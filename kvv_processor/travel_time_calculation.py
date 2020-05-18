from kvv_processor.model.trip_section import TripSection
from kvv_processor.line_route_mapper import LineRouteMapper

import logging
from datetime import timedelta

logger = logging.getLogger(__name__)


class TravelTimeCalculator:
    def __init__(self, trip_repository, route_repository, stop_time_repository, trip_section_repository, stop_repository, time_parser):
        self.time_parser = time_parser
        self.trip_repository = trip_repository
        self.route_repository = route_repository
        self.stop_time_repository = stop_time_repository
        self.trip_section_repository = trip_section_repository()
        self.stop_repository = stop_repository()
        self.line_route_mapper = LineRouteMapper(self.trip_repository,
                                                 self.route_repository,
                                                 self.stop_repository,
                                                 self.stop_time_repository)

    def calculate_travel_times(self, lines):

        for line in lines:

            logger.info('process line %s', line.line_id)
            trip = self.line_route_mapper.map_line(line)
            trip_sections = self.trip_section_repository.trip_sections_for_line(
                line.line_id)

            if trip and not trip_sections:

                stop_times = self.stop_time_repository.find_stops_by_trip_id(
                    trip.trip_id)

                for i in range(len(stop_times) - 2):
                    trip_section = self.create_trip_section(
                        stop_times[i], stop_times[i + 1], trip, line.line_id)
                    self.trip_section_repository.insert(trip_section)
                    logger.info(str(trip_section))

                last_section = stop_times[-2:]
                last_trip_section = self.create_trip_section(
                    last_section[0], last_section[1], trip, line.line_id)
                logger.info(str(last_trip_section))

                self.trip_section_repository.insert(last_trip_section)

    def create_trip_section(self, stop_time_from, stop_time_to, trip, line_id):
        travel_time = self.calcluate_travel_time(stop_time_from, stop_time_to)
        travel_time_seconds = travel_time.total_seconds()
        return TripSection(trip.trip_id, line_id, stop_time_from.stop_id,
                           stop_time_to.stop_id, travel_time_seconds)

    def calcluate_travel_time(self, stop_time_from, stop_time_to):
        departure = self.time_parser.parse(stop_time_from.departure_time)
        arrival = self.time_parser.parse(stop_time_to.arrival_time)

        if arrival < departure:
            negative_time = arrival - departure
            return negative_time + timedelta(days=1)

        return arrival - departure
