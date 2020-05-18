from machine_learning.model.combined_report import CombinedReport
from machine_learning.prepsocessing.data_map import DataMap
from machine_learning.neural_network.accuracy import Accuracy

from machine_learning.model.ml_delay_class import MLDelayClass
from machine_learning.model.ml_travel_time import MLTravelTime
import logging
logger = logging.getLogger(__name__)

class CombinedPrediction(object):
    def __init__(self, classificator, regressor):
        self.classificator = classificator
        self.regressor = regressor

    def analyse(self, data_loader, line_id, line_id_official):
        data_map = data_loader.load(line_id, line_id_official)
        self.classificator.train(
            data_map.data_train[MLDelayClass.x_features].values,
            data_map.data_train[MLDelayClass.y_feature].values)
        self.regressor.train(
            data_map.data_train[MLTravelTime.x_features].values,
            data_map.data_train[MLTravelTime.y_feature].values)

        test_prediction = self._prediction(
            data_map.data_test[MLDelayClass.x_features].values,
            data_map.data_test[MLTravelTime.x_features].values,
            data_map.data_test['planned_travel_time'].values)
        logger.info('Accuracy: %s', Accuracy.reg(test_prediction, data_map.data_test[MLTravelTime.y_feature].values))
        test_prediction_neo = self._prediction(
            data_map.data_neo[MLDelayClass.x_features].values,
            data_map.data_neo[MLTravelTime.x_features].values,
            data_map.data_neo['planned_travel_time'].values)
        logger.info('Accuracy Neo: %s',Accuracy.reg(test_prediction_neo, data_map.data_neo[MLTravelTime.y_feature].values))

    def _prediction(self, delay_x, travel_time_x, planned_travel_times):
        classification_prediction = self.classificator.predict(delay_x)
        regressor_prediction = self.regressor.predict(travel_time_x)
        prediction = []

        # 1.0 => no delay
        for i, class_prediction in enumerate(classification_prediction):
            if class_prediction == 1.0:
                prediction.append(regressor_prediction[i])
            if class_prediction == 0.0:
                prediction.append(planned_travel_times[i])
        return prediction
