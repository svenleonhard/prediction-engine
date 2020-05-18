from machine_learning.prepsocessing.data_map_categories_benchmark import DataMapCategoriesBenchmark
from machine_learning.prepsocessing.data_map_benchmark import DataMapBenchmark
import pandas as pd
import csv, yaml

class DataMapIO(object):

    def __init__(self, line_id=0):
        self.line_id = line_id

    def read(self, model):
        df = self._read_df(model.y_feature)
        categories = self._read_categories(model.y_feature)
        return DataMapCategoriesBenchmark(df, model.x_features, model.y_feature, categories, model.benchmark)

    def write(self, data_map):
        self._write_df(data_map.df, data_map.y_feature)
        if isinstance(data_map, DataMapCategoriesBenchmark):
            self._write_categories(data_map.categories, data_map.y_feature)

    def _read_df(self, name):
        df = pd.read_csv( self._file_name(name))
        return df.drop(df.columns[0], axis=1)

    def _read_categories(self, name):
        file_path = self._file_name(name, 'categories_', ending='yaml')
        with open(file_path, 'r') as stream:
            return yaml.safe_load(stream)

    def _write_df(self, df, name):
        df.to_csv(self._file_name(name))

    def _write_categories(self, categories, name):
        with open(self._file_name(name, 'categories_', ending='yaml'), 'w') as outfile:
            yaml.dump(categories, outfile)
    
    def _file_name(self, name, prefix='', ending='csv'):
        return ''.join(['datasets/', prefix, name, '.', ending])
