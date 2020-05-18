from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from machine_learning.helper.metric_calculator import MetricCalculator
from machine_learning.helper.conditions.range import RangeCondition
from machine_learning.helper.conditions.equal import EqualCondition
import logging

logger = logging.getLogger(__name__)

class Report:

    def __init__(self, expected, actual, benchmark=[]):
        self.expected = expected
        self.actual = actual
        self.benchmark = benchmark
        self.variance = explained_variance_score(self.expected, self.actual)
        self.mse = mean_squared_error(self.expected, self.actual)
        self.mae = mean_absolute_error(self.expected, self.actual)
        self.accuracy = self._accuracy(self.actual, self.expected)
        self.benchmark_accuracy = self._accuracy(self.benchmark, self.expected)
    
    def print(self):
        logger.info('Report')
        logger.info(self.actual)
        logger.info('Variance: %s' % self.variance)
        logger.info('MSE: %s' % self.mse)
        logger.info('MAE: %s' % self.mae)
        logger.info('Expected: %s' % self.expected)
        logger.info('Actual: %s', self.actual)
        logger.info('Benchmark: %s', self.benchmark)
        logger.info('Accuracy: %s' % self.accuracy)
        logger.info('Benchmark Accuracy: %s' % self.benchmark_accuracy)
        logger.info('Range accuracy prediction: %s', self._range_accuracy(self.actual, self.expected))
        logger.info('Range accuracy benchmark: %s', self._range_accuracy(self.benchmark, self.expected))

    def _accuracy(self, actual, expected):
        if len(actual) == 0:
            return 0
        return MetricCalculator.calculate(actual, expected, EqualCondition)

    def _range_accuracy(self, actual, expected):
        if len(actual) == 0:
            return 0
        return MetricCalculator.calculate(actual, expected, RangeCondition)
