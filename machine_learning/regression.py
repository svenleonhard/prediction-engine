class Regression(object):

    def __init__(self, regressor, scaler):
        self.scaler = scaler
        self.regressor = regressor

    def train(self, x_train, y_train):
        self.scaler.fit(x_train)
        x_train = self.scaler.transform(x_train)
        self.regressor.fit(x_train, y_train)
    
    def predict(self, x):
        x = self.scaler.transform(x)
        prediction = self.regressor.predict(x)
        return prediction
