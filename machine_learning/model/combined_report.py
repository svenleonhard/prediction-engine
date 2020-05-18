from machine_learning.model.report import Report

import logging

logger = logging.getLogger(__name__)

class CombinedReport(object):

    def __init__(self, delayed_data_map, delay_prediction, on_time_data_map):
        self.delayed_data_map = delayed_data_map
        self.delay_prediction = delay_prediction
        self.on_time_data_map = on_time_data_map

    def print_report(self):
        report_delay = Report(self.delayed_data_map.y_valid, self.delay_prediction, 'Valid Delay')
        report_on_time = Report(self.on_time_data_map.y_valid, self.on_time_data_map.valid_benchmark, 'Valid On Time')
        n_delay = len(self.delayed_data_map.x_valid)
        n_on_time = len(self.on_time_data_map.x_valid)
        n_all = n_delay + n_on_time
        accuracy = self._calculate_accuracy(report_delay.accuracy, report_on_time.accuracy,n_delay,n_on_time, n_all)
        
        logger.info('Delay Accuracy: %s', report_delay.accuracy)
        logger.info('On Time Accuracy: %s', report_on_time.accuracy)
        logger.info('Accuracy: %s', accuracy)

    def _calculate_accuracy(self, delayed_accuracy, on_time_accuracy, n_delay, n_on_time, n_all):
        accuracy = (n_delay / n_all) * delayed_accuracy + (n_on_time / n_all) * on_time_accuracy
        return accuracy
