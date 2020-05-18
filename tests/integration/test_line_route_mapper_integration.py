from kvv_processor.line_route_mapper import LineRouteMapper
from kvv_processor.model.line import Line
from kvv_processor.kvv_processor_di_container import KvvProcessorDIContainer

import unittest


class TestLineRouteMapperIntegration(unittest.TestCase):
    def setUp(self):
        kvv_processor_di_container = KvvProcessorDIContainer()
        trip_repository = kvv_processor_di_container.trip_repository()
        route_repository = kvv_processor_di_container.route_repository()
        stop_repository = kvv_processor_di_container.stop_repository()
        stop_time_repository = kvv_processor_di_container.stop_time_repository()

        self.line_route_mapper = LineRouteMapper(trip_repository,
                                                 route_repository,
                                                 stop_repository,
                                                 stop_time_repository)
        self.line = Line(1, 'S-Bahn S5', 'S5 Wörth Badepark')

    def test_map_line(self):
        trip = self.line_route_mapper.map_line(self.line)
        self.assertTrue(trip)

if __name__ == '__main__':
    unittest.main()