from k_nearest_neighbour.knn_delay import KNNDelay
from kvv_processor.model.station import Station
from machine_learning.model.report import Report
import numpy as np

import logging

logger = logging.getLogger(__name__)

class KNNService(object):

    def __init__(self, knn_calculator, post_optimizer):
        self.knn_calculator = knn_calculator
        self.post_optimizer = post_optimizer
        self.maximum_batch = 100

    def analyse(self, data_loader, official_line_id, line_id):
        data_map = data_loader.load(official_line_id)
        knn_delays = self.create_knn_delay_list(data_map, official_line_id, line_id)
        predicted_delays = self.predict_delays(knn_delays)
        predicted_delays = self.post_optimizer.optimize(predicted_delays)
        expected_delays = self.extract_expected_delays(data_map, predicted_delays)
        Report(expected_delays, predicted_delays, data_map.test_benchmark).print()

    def predict_delays(self, knn_delays):
        predicted_delays = []
        for i, knn_delay in enumerate(knn_delays):
            delay_prediction = self.knn_calculator.predict(knn_delay)
            predicted_delays.append(delay_prediction)
            logger.info('Predict record %s',i)
        logger.info('Number of prediction records: %s', len(predicted_delays))
        return np.asarray(predicted_delays)

    def extract_expected_delays(self, data_map, predicted_delays):
        expected = data_map.y
        if len(predicted_delays) < len(data_map.y):
            expected = expected[:len(predicted_delays)]
        logger.info('Number of expected records : %s', len(data_map.y))
        return np.asarray(expected)

    def create_knn_delay_list(self, data_map, official_line_id, line_id):
        knn_delays = []
        for index, row in data_map.df.iterrows():
            if index == self.maximum_batch:
                return knn_delays
            delay = int(row['current_delay'])
            previous_station = Station(data_map.categories['station'][row['station']])
            target_station = Station(data_map.categories['target_station'][row['target_station']])
            knn_delay = KNNDelay(delay,official_line_id, line_id, previous_station, target_station)
            knn_delays.append(knn_delay)

        return knn_delays
