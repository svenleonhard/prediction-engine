from kvv_processor.kvv_processor_service import KvvProcessorService
from machine_learning.prepsocessing.data_map import DataMap
from machine_learning.prepsocessing.data_map_categories_benchmark import DataMapCategoriesBenchmark
from machine_learning.model.ml_delay import MLDelay
from machine_learning.helper.data_map_io import DataMapIO
from machine_learning.factorires.random_sections import RandomSections
from machine_learning.factorires.data_map_factory import DataMapFactory
from collections import defaultdict
import pandas as pd
import logging
import random as rndm

logger = logging.getLogger(__name__)

class DataLoader(object):

    def __init__(self, validator, random_sections, model=MLDelay):
        self.kvv_processor_service = KvvProcessorService()
        self.nn_data = []
        self.min_trip_len = 3
        self.categories = {}
        self.validator = validator
        self.model = model
        self.random_sections = random_sections
    
    def load(self, line_id, line_id_official):
        # return self.load_data_map(line_id)
        # return self._load_from_database(line_id)
        data_map = self._load_from_database(line_id)
        data_map_neo = self._load_from_database(line_id_official)
        data_map.add_neo(data_map_neo.df)
        return data_map

    def load_data_map(self, line_id):
        try:
            return self._load_from_file(line_id)
        except:
            logger.info('Data Map not chached, auto load from database')
            return self._load_from_database(line_id)
        
    def _load_from_file(self, line_id):
        return DataMapIO(line_id).read(self.model)

    def _load_from_database(self, line_id):
        trips = self.load_trips(line_id)
        trips = self.clean_trips(trips)
        trips = self.validator.check(trips)
        sections = self.create_sections(trips)
        return DataMapFactory().create_from(sections, self.model)

    def create_sections(self, trips):
        sections = []
        for trip in trips:
            sections = sections + self.random_sections.create(trip, self.model)
        return sections

    def load_trips(self, line_id):
        stops = self.kvv_processor_service.stops_for_line(line_id)
        return self.group_by_journey(stops)

    def clean_trips(self, trips):
        cleaned_trips = []
        for trip in trips:
            if len(trips[trip]) >= self.min_trip_len:
                cleaned_trips.append(trips[trip])
        return cleaned_trips

    def group_by_journey(self, stops):
        groups = defaultdict(list)
        
        for stop in stops:
            groups[stop.journey_id].append(stop)
        return groups
