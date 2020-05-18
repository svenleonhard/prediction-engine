from kvv_processor.kvv_processor_service import KvvProcessorService
import unittest


class TestKvvProcessorServiceIntegration(unittest.TestCase):
    def setUp(self):
        self.kvv_processor_service = KvvProcessorService()

    def test_neo_stops_for_line(self):
        stops = self.kvv_processor_service.neo_stops_for_line('kvv:21003:E:H')
        self.assertIsNotNone(stops)
        self.assertGreater(len(stops), 0)

    def test_stops_for_line(self):
        stops = self.kvv_processor_service.stops_for_line(39)
        self.assertIsNotNone(stops)
        self.assertGreater(len(stops), 0)

        stops = self.kvv_processor_service.stops_for_line('kvv:21003:E:H')
        self.assertIsNotNone(stops)
        self.assertGreater(len(stops), 0)

if __name__ == '__main__':
    unittest.main()