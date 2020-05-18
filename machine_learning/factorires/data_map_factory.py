from machine_learning.prepsocessing.data_map_categories_benchmark import DataMapCategoriesBenchmark
from machine_learning.helper.data_map_io import DataMapIO
import pandas as pd

class DataMapFactory(object):

    def create_from(self, sections, model):
        df = pd.DataFrame([stop.__dict__ for stop in sections])
        categories, categorized_df = self._categorize(df, model.non_numeric)

        data_map = DataMapCategoriesBenchmark(categorized_df, model.x_features, model.y_feature,categories, model.benchmark)
        DataMapIO().write(data_map)
        return data_map

    def _categorize(self, df, to_categorize):
        categories = {}
        for category in to_categorize:
            data_cat = pd.DataFrame()
            data_cat[category] = df[category].astype('category')
            df[category] = df[category].astype('category').cat.codes
            categories[category] = data_cat[category].cat.categories.values.tolist()
        return categories, df
        