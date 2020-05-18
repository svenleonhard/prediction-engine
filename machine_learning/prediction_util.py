import logging, copy

logger = logging.getLogger(__name__)

class PredictionUtil:

    def __init__(self, predictor, report):
        self.predictor = predictor
        self.report = report

    def analyse(self, data_loader, line_id, line_id_official):
        data_map = data_loader.load(line_id, line_id_official)
        self.training(data_map)
        prediction = self.prediction(data_map.x_test)
        self.report(data_map.y_test, prediction, data_map.test_benchmark).print()
        prediction = self.prediction(data_map.x_neo)
        self.report(data_map.y_neo, prediction, data_map.neo_benchmark).print()
        

    def training(self, data_map):
        self.predictor.train(data_map.x_train, data_map.y_train)

    def prediction(self, x):
        return self.predictor.predict(x)
