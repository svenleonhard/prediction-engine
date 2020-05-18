from machine_learning.prepsocessing.data_map_categories import DataMapCategories

class DataMapCategoriesBenchmark(DataMapCategories):

    def __init__(self, df, x_features, y_feature, categories, benchmark):
        DataMapCategories.__init__(self, df, x_features, y_feature, categories)

        self.benchmark = benchmark
        
        self.train_benchmark = self.data_train[benchmark].values
        self.valid_benchmark = self.data_valid[benchmark].values
        self.test_benchmark = self.data_test[benchmark].values