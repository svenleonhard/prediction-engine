from kvv_processor.repositories.weather_repository import WeatherRepository
from kvv_processor.kvv_processor_di_container import KvvProcessorDIContainer
import unittest


class TestWeatherRepositoryIntegration(unittest.TestCase):
    def setUp(self):
        self.weather_repository = KvvProcessorDIContainer().weather_repository()

    def test_find_weather_by_stop_id(self):
        result = self.weather_repository.find_weather_by_stop_id(28)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
