from kvv_processor.kvv_processor_service import KvvProcessorService
from kvv_processor.model.journey import Journey
from kvv_processor.model.stop import Stop
from kvv_processor.repositories.trip_section_repository import TripSectionRepository
from kvv_processor.repositories.stop_repository import StopRepository

import logging

import datetime
from datetime import timedelta

logger = logging.getLogger(__name__)


class Journey_Calculator:
    def __init__(self):
        self.kvv_processor_service = KvvProcessorService()
        self.journey_id = 0
        self.travel_times = []

    def calculate_journeys_for_line(self, line_id):

        trip_sections = self.kvv_processor_service.trip_sections_by_line(
            line_id)

        if not trip_sections:
            return

        stop_index = 0

        time = datetime.datetime(2018, 12,10)
        stops_for_line = self.kvv_processor_service.basic_stops_for_line(line_id, time)
        logger.info('Start with journey 0')

        while len(stops_for_line) > 0:
            logger.debug('Line %s Stops left: %s', line_id,
                         len(stops_for_line))

            if stop_index is None:
                logger.warning('No stop index found - aborted')
                return

            current_stop = stops_for_line[stop_index]
            semantic_journey_id = str(line_id) + '-' + str(self.journey_id)
            journey = Journey(semantic_journey_id, current_stop.stop_id)
            self.write_journey_to_db(journey)
            stops_for_line.remove(current_stop)

            next_trip_section = self.find_next_trip_section(
                current_stop, trip_sections)

            if next_trip_section:
                stop_index = self.find_index_next_stop(current_stop,
                                                       next_trip_section,
                                                       stops_for_line,
                                                       trip_sections)
            else:
                self.increment_journey_id()

    @classmethod
    def find_next_trip_section(self, current_stop, trip_sections):

        for trip_section in trip_sections:
            if trip_section.station_from.compare(current_stop.station_id):
                return trip_section

    def find_index_next_stop(self, current_stop, trip_section, stops_for_line,
                             trip_sections):

        destination_departure = current_stop.time_tabled_time + timedelta(
            seconds=trip_section.travel_time)

        for i, stop_for_line in enumerate(stops_for_line):

            if stop_for_line.time_tabled_time > destination_departure:
                new_curent_stop = Stop(0, trip_section.station_to, 0,
                                       destination_departure,
                                       destination_departure, self.journey_id)
                next_trip_section = self.find_next_trip_section(
                    new_curent_stop, trip_sections)
                if next_trip_section:
                    return self.find_index_next_stop(new_curent_stop,
                                                     next_trip_section,
                                                     stops_for_line,
                                                     trip_sections)
                self.increment_journey_id()
                return 0

            if stop_for_line.time_tabled_time == destination_departure and trip_section.station_to.compare(
                    stop_for_line.station_id):
                return i

    def write_journey_to_db(self, journey):
        self.kvv_processor_service.insert_journey(journey)

    def increment_journey_id(self):
        self.journey_id = self.journey_id + 1
        logger.info('new journey id: %s', self.journey_id)
