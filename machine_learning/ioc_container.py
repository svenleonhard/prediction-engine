from machine_learning.prepsocessing.data_loader import DataLoader
from machine_learning.factorires.travel_time_section_factory import TravelTimeSectionFactory
from machine_learning.model.ml_travel_time import MLTravelTime
from machine_learning.model.ml_travel_time_class import MLTravelTimeClass
from machine_learning.model.ml_delay_class import MLDelayClass
from machine_learning.prepsocessing.data_map import DataMap
from machine_learning.postprocessing.post_optimizer import PostOptimizer
from machine_learning.prepsocessing.delay_filter import DelayFilter
from machine_learning.prepsocessing.validator import Validator
from machine_learning.prediction_util import PredictionUtil
from machine_learning.model.nn_config import NNConfig
from machine_learning.regression import Regression
from kvv_processor.kvv_processor_service import KvvProcessorService
from k_nearest_neighbour.knn_service import KNNService
from k_nearest_neighbour.knn_calculator import KNNCalculator
from machine_learning.combined_prediction import CombinedPrediction
from machine_learning.neural_network.class_net import ClassNet
from machine_learning.neural_network.class_net_adapter import ClassNetAdapter
from machine_learning.neural_network.regression_net_adapter import RegressionNetAdapter
from machine_learning.model.nn_class_config import NNClassConfig
from machine_learning.optimized_predictor import OptimizedPredictor
from machine_learning.model.report import Report
from machine_learning.model.report_nn import ReportNN
from machine_learning.network import Network
from machine_learning.factorires.random_sections import RandomSections

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.svm import SVR
import dependency_injector.containers as containers
import dependency_injector.providers as providers
import logging, yaml

logger = logging.getLogger(__name__)

class IoCContainer(containers.DeclarativeContainer):

    # Helper
    post_optimizer = providers.Factory(PostOptimizer)
    delay_filter = providers.Factory(DelayFilter)
    standard_scaler = providers.Factory(StandardScaler)
    validator = providers.Factory(Validator)
    
    # Data Loading
    kvv_processor_service = providers.Factory(KvvProcessorService)
    random_sections = providers.Factory(RandomSections, kvv_processor_service=kvv_processor_service)
    data_loader_delay = providers.Factory(DataLoader, validator=validator, random_sections=random_sections)
    data_loader_delay_class = providers.Factory(DataLoader, validator=validator,random_sections=random_sections, model=MLDelayClass)
    travel_time_section_factory = providers.Factory(TravelTimeSectionFactory)
    data_loader_travel_time = providers.Factory(DataLoader, validator=validator, random_sections=random_sections, model=MLTravelTime)
    data_loader_travel_time_class = providers.Factory(DataLoader, validator=validator,random_sections=random_sections, model=MLTravelTimeClass)
    data_map = providers.Factory(DataMap)

    # Neural Network
    config = providers.Configuration('config')
    
    travel_time_config = providers.Factory(NNClassConfig,config_dict=config.travel_time_network)
    travel_time_network = providers.Factory(Network, nn_config=travel_time_config)
    travel_time_network_predictor = providers.Factory(OptimizedPredictor, predictor=travel_time_network, optimizer=post_optimizer)
    travel_time_network_util = providers.Factory(PredictionUtil, predictor=travel_time_network_predictor, report=Report)
    
    class_network_config = providers.Factory(NNClassConfig,config_dict=config.class_network)
    class_network_adapter = providers.Factory(ClassNetAdapter, nn_config=class_network_config)
    class_util = providers.Factory(PredictionUtil, predictor= class_network_adapter, report=ReportNN)
    
    # Regression Models
    k_nearest_neighbour = providers.Factory(KNeighborsRegressor,n_neighbors=config.k_nearest_neighbour.n_neighbors, weights=config.k_nearest_neighbour.distance)
    knn_wrapper = providers.Factory(Regression, scaler=standard_scaler, regressor=k_nearest_neighbour)
    knn_predictor = providers.Factory(OptimizedPredictor, predictor=knn_wrapper, optimizer=post_optimizer)
    prediction_util_knn = providers.Factory(PredictionUtil, predictor=knn_predictor, report=Report)

    knn_class = providers.Factory(KNeighborsClassifier,n_neighbors=config.k_nearest_neighbour.n_neighbors, weights=config.k_nearest_neighbour.distance)
    knn_class_wrapper = providers.Factory(Regression, scaler=standard_scaler, regressor=knn_class)
    prediction_util_knn_class = providers.Factory(PredictionUtil, predictor=knn_class_wrapper, report=Report)

    svr = providers.Factory(SVR, kernel='rbf', C=200, gamma=0.2)
    svr_wrapper = providers.Factory(Regression, scaler=standard_scaler, regressor=svr)
    svr_predictor = providers.Factory(OptimizedPredictor, predictor=svr_wrapper, optimizer=post_optimizer)
    prediction_util_svr = providers.Factory(PredictionUtil, predictor=svr_predictor, report=Report)

    # Custom KNN
    knn_calculator = providers.Factory(KNNCalculator)
    knn_service = providers.Factory(KNNService,knn_calculator=knn_calculator, post_optimizer=post_optimizer)

    # Classification Models
    svm = providers.Factory(SVC, kernel='rbf')
    svm_wrapper = providers.Factory(Regression, scaler=standard_scaler, regressor=svm)
    prediction_util_svm_class = providers.Factory(PredictionUtil, predictor=svm_wrapper, report=Report)

    # Combined
    combined_prediction = providers.Factory(CombinedPrediction, classificator=class_network_adapter, regressor=svr_predictor)
