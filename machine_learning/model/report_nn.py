from sklearn.metrics import confusion_matrix, classification_report

import logging

logger = logging.getLogger(__name__)
class ReportNN(object):

    def __init__(self, expected, actual, benchmark=[]):
        self.expected = expected
        self.actual = actual
        self.benchmark = benchmark

    def print(self):
        confusion_matrix(self.expected, self.actual)
        logger.info(classification_report(self.expected, self.actual))

