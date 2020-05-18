from kvv_processor.repositories.weather_repository import WeatherRepository
import logging
import random as rndm

logger = logging.getLogger(__name__)

class RandomSections(object):

    def __init__(self, kvv_processor_service):
        self.kvv_processor_service = kvv_processor_service

    def create(self, trip, model):
        random_sections = []
        for i, stop in enumerate(trip[:-1]):
            idx = i + 1
            target = rndm.randint(idx, len(trip) - 1)
            try:
                # self.weather_repository.find_weather_by_stop_id(stop.stop_id)
                random_sections.append(model(stop, trip[target]))
            except TypeError as e:
                logger.error(e)
            except AttributeError as e:
                logger.error(e)
            except Exception as e:
                logger.error(e)
        return random_sections
