from kvv_processor.repositories.stop_repository import StopRepository
from kvv_processor.repositories.trip_section_repository import TripSectionRepository
from kvv_processor.helper.time_parser import TimeParser
from kvv_processor.kvv_processor_di_container import KvvProcessorDIContainer
from statistics import mean
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)


class KNNCalculator:
    def __init__(self):
        self.k = 10
        self.stop_repository = KvvProcessorDIContainer().stop_repository()
        self.trip_section_repository = KvvProcessorDIContainer().trip_section_repository()
        self.time_parser = TimeParser()

    def predict(self, knn_delay):
        k_stops = self.find_k_stops(knn_delay.delay, knn_delay.line_id,
                                    knn_delay.previous_station)
        average_delay = self.calculate_average_delay(
            k_stops, knn_delay.target_station)
        return average_delay

    def find_k_stops(self, delay, line_id, previous_station):
        stops = []
        index = 0
        while len(stops) < self.k:
            stops = self.stops_by_delay(line_id, previous_station, delay, index)

            if len(stops) >= self.k or index == 29:
                return stops[:self.k]
            index = index + 1
        return stops

    def stops_by_delay(self, line_id, station, delay, index):
        delay_offset = int(index / 12) * 60
        min_delay = delay - delay_offset
        max_delay = delay + delay_offset

        return self.stop_repository.stops_by_delay_time_range(
            line_id,
            station.id_shorted,
            min_delay=min_delay,
            max_delay=max_delay)

    def calculate_average_delay(self, stops, target_station):
        delays = []
        for stop in stops:
            try:
                travel_time = self.calculate_delay(stop, target_station)
                delays.append(travel_time)
            except Exception as e:
                logger.error(e)

        if len(delays) == 0:
            logger.warning('No Delays found')
            return 0

        return int(mean(delays))

    def calculate_delay(self, stop, target_station):
        stop_journey_id = self.stop_repository.stop_journey_id(stop.stop_id)
        target_stop = self.find_target_stop(stop_journey_id, target_station)
        return target_stop.delay() - stop.delay()


    def find_target_stop(self, stop_journey_id, target_station):
        target_stop = self.stop_repository.stop_for_journey(
            stop_journey_id, target_station.id_shorted)
        return target_stop
