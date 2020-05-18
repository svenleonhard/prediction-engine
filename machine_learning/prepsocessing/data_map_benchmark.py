from machine_learning.prepsocessing.data_map import DataMap

class DataMapBenchmark(DataMap):

    def __init__(self, df, x_features, y_feature, benchmark):

        DataMap.__init__(self, df, x_features, y_feature)

        self.train_benchmark = self.data_train[benchmark].values
        self.valid_benchmark = self.data_valid[benchmark].values
        self.test_benchmark = self.data_test[benchmark].values
