from kvv_processor.kvv_processor_di_container import KvvProcessorDIContainer
import unittest


class TestStopRepositoryIntegration(unittest.TestCase):
    def setUp(self):
        self.stop_repository = KvvProcessorDIContainer().stop_repository()

    def test_number_of_stations(self):
        number_of_stations = self.stop_repository.number_of_stations(1)
        self.assertTrue(number_of_stations)
        self.assertEqual(number_of_stations, 86)

    def test_stop_for_journey(self):
        stop_for_journey = self.stop_repository.stop_for_journey(
            '39-39990', 'de:08212:12')
        self.assertIsNotNone(stop_for_journey)
        self.assertEqual(stop_for_journey.stop_id, 13958342)

    def test_stop_journey_id(self):
        journey_id = self.stop_repository.stop_journey_id('13958342')
        self.assertEqual(journey_id, '39-39990')


if __name__ == '__main__':
    unittest.main()