import numpy as np

class DataMap(object):

    def __init__(self, df, x_features, y_feature):
        self.y_feature = y_feature
        self.x_features = x_features
        self.df = df
        self.y = self.df[self.y_feature].values
        df = df.sample(n = len(df))
        df = df.reset_index(drop=True)

        data_valid_test = df.sample(frac=0.3)
        self.data_test = data_valid_test.sample(frac=0.5)
        self.data_valid = data_valid_test.drop(self.data_test.index)
        self.data_train = df.drop(data_valid_test.index)

        self.x_train = self.data_train[self.x_features].values
        self.x_valid = self.data_valid[self.x_features].values
        self.x_test = self.data_test[self.x_features].values

        self.y_train = self.data_train[self.y_feature].values
        self.y_valid = self.data_valid[self.y_feature].values
        self.y_test = self.data_test[self.y_feature].values

    def add_neo(self, df):
        self.x_neo = df[self.x_features].values
        self.y_neo = df[self.y_feature].values
        self.neo_benchmark = df['planned_travel_time'].values
        self.data_neo = df
