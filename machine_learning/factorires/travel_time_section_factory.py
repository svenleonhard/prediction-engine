from machine_learning.model.ml_travel_time import MLTravelTime
import numpy as np

class TravelTimeSectionFactory(object):
    
    def create_travel_time_section(self, stop, target_stop, trip_sections):
        self.trip_sections = trip_sections
        trip_section = self._find_trip_section(stop.station_id, stop.line_id)
        return MLTravelTime(stop, target_stop)

    def _find_trip_section(self, start_station, line_id):
        for trip_section in self.trip_sections:
            if trip_section.line_id == line_id and trip_section.station_from.compare(start_station):
                return trip_section
