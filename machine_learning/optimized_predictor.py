class OptimizedPredictor(object):

    def __init__(self, predictor, optimizer):
        self.predictor = predictor
        self.optimizer = optimizer

    def train(self, x_train, y_train):
        self.predictor.train(x_train, y_train)

    def predict(self, x):
        prediction = self.predictor.predict(x)
        return self.optimizer.optimize(prediction)
