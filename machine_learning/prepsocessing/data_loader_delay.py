from machine_learning.prepsocessing.data_loader import DataLoader
from machine_learning.prepsocessing.data_map import DataMap
from machine_learning.prepsocessing.data_map_categories_benchmark import DataMapCategoriesBenchmark
from machine_learning.model.ml_delay import MLDelay
from machine_learning.helper.data_map_io import DataMapIO
import pandas as pd
import random as rndm
import logging

logger = logging.getLogger(__name__)

class DataLoaderDelay(DataLoader):

    def __init__(self, validator, model=MLDelay):
        DataLoader.__init__(self, validator=validator, model=model)
    
    def load(self, line_id):
        try:
            return self._load_from_file()
        except:
            logger.info('Data Map not chached, auto load from database')
        return self._load_from_database(line_id)
        
    def _load_from_file(self):
        return DataMapIO().read(self.model)

    def _load_from_database(self, line_id):
        cleaned_trips = self.load_trips(line_id)
        for trip in cleaned_trips:
            self.random_target_stops(trip)
        df = pd.DataFrame([stop.__dict__ for stop in self.nn_data])
        categories, categorized_df = self.categorize(df, self.model.non_numeric)

        data_map = DataMapCategoriesBenchmark(categorized_df, self.model.x_features, self.model.y_feature,categories, self.model.benchmark)
        DataMapIO().write(data_map)
        return data_map

    def random_target_stops(self, trip):
        for i, stop in enumerate(trip):
            idx = i + 1
            if idx == len(trip):
                return
            target = rndm.randint(idx, len(trip) - 1)
            try:
                self.nn_data.append(self.model(stop, trip[target]))
            except TypeError as e:
                logger.error(e)
            except AttributeError as e:
                logger.error(e)

    def sort_stops(self, stops):
        return sorted(stops, key=lambda stop: stop.time_tabled_time)
