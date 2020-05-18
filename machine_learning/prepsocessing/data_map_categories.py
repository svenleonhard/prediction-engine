from machine_learning.prepsocessing.data_map import DataMap

class DataMapCategories(DataMap):

    def __init__(self, df, x_features, y_feature, categories):
        DataMap.__init__(self, df, x_features, y_feature)
        self.categories = categories