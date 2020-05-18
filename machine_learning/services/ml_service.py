from machine_learning.ioc_container import IoCContainer
from machine_learning.model.ml_delay import MLDelay
from machine_learning.model.ml_delay_class import MLDelayClass
from machine_learning.model.ml_travel_time import MLTravelTime
import yaml, logging

logger = logging.getLogger(__name__)

class MLService:

    def __init__(self):
        self.ioc_container = IoCContainer(config=self._load_network_config())
        self.data_loader_travel_time = self.ioc_container.data_loader_travel_time()
        self.data_loader_delay = self.ioc_container.data_loader_delay()
        self.data_loader_delay_class = self.ioc_container.data_loader_delay_class()
        self.data_loader_travel_time_class = self.ioc_container.data_loader_travel_time_class()

    def travel_time_neural_network_for(self, line_id, line_id_official):
        self.ioc_container.travel_time_network_util().analyse(self.data_loader_travel_time, line_id, line_id_official)

    def punctuality_class_network_for(self, line_id):
        self.ioc_container.class_util().analyse(self.data_loader_delay_class, line_id)

    def travel_time_class_svm(self, line_id, line_id_official):
        self.ioc_container.prediction_util_svm_class().analyse(self.data_loader_travel_time_class, line_id, line_id_official)

    def custom_knn(self, line_id, line_id_official):
        self.ioc_container.knn_service().analyse(self.data_loader_delay, line_id, line_id_official)

    def general_knn_regression(self, line_id, line_id_official):
        self.ioc_container.prediction_util_knn().analyse(self.data_loader_travel_time, line_id, line_id_official)

    def general_knn_class(self, line_id, line_id_official):
        self.ioc_container.prediction_util_knn_class().analyse(self.data_loader_travel_time_class, line_id, line_id_official)

    def svr(self, line_id, line_id_official):
        self.ioc_container.prediction_util_svr().analyse(self.data_loader_travel_time, line_id, line_id_official)

    def combined_prediction(self, line_id, line_id_official):
        self.ioc_container.combined_prediction().analyse(self.data_loader_delay_class, line_id, line_id_official)

    def _load_network_config(self):
        with open('machine_learning/config/prediction_config.yaml', 'r') as stream:
            try:
                config = yaml.safe_load(stream)
                config['travel_time_network']['n_feature'] = len(MLTravelTime.x_features)
                config['delay_network']['n_feature'] = len(MLDelay.x_features)
                config['class_network']['n_feature'] = len(MLDelayClass.x_features)
                return config
            except yaml.YAMLError as e:
               logger.error(e)
