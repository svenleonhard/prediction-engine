import pandas as pd
from machine_learning.prepsocessing.data_map_categories_benchmark import DataMapCategoriesBenchmark
import logging

logger = logging.getLogger(__name__)

class DelayFilter(object):

    def delayed(self, data_map):
        df =  data_map.df.copy()
        filtered_df = df[df.current_delay != 0]
        return DataMapCategoriesBenchmark(filtered_df, data_map.x_features, data_map.y_feature, data_map.categories, data_map.benchmark)
    
    def on_time(self, data_map):
        df =  data_map.df.copy()
        filtered_df = df[df.current_delay == 0]
        return DataMapCategoriesBenchmark(filtered_df, data_map.x_features, data_map.y_feature, data_map.categories, data_map.benchmark)
