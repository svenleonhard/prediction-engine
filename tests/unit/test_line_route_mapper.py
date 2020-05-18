from kvv_processor.line_route_mapper import LineRouteMapper
from kvv_processor.model.line import Line
from kvv_processor.model.trip import Trip
from kvv_processor.model.route import Route

import unittest
from unittest.mock import Mock

class TestLineRouteMapper(unittest.TestCase):

    def setUp(self):
        trip_repository = Mock()
        route_repository = Mock()
        stop_repository = Mock()
        stop_time_repository = Mock()

        trips = [
            Trip('80.T3.21-1-E-s19-10.4.R', '21-1-E-s19-10','1 Durlach'),
            Trip('10.T2.21-1-E-s19-1.1.R', '21-1-E-s19-1','1 Durlach')
        ]

        trip_repository.find_trips_by_trip_headsign.return_value = trips

        route_repository.find_route_by_route_id.return_value = Route('21-1-E-s19-10', '1', '0')
        stop_repository.number_of_stations.return_value = 2
        stop_time_repository.number_of_stations.return_value = 2

        self.line_route_mapper = LineRouteMapper(trip_repository, route_repository, stop_repository, stop_time_repository)
        self.line = Line(1, 'Straßenbahn 1', '1 Durlach')

    def test_map_line(self):
        trip = self.line_route_mapper.map_line(self.line)
        self.assertEqual(trip.trip_id, '80.T3.21-1-E-s19-10.4.R')

if __name__ == '__main__':
    unittest.main()
