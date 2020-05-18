import logging
from context import machine_learning
from machine_learning.services.ml_service import MLService

logger = logging.getLogger(__name__)
LINE = 18
LINE_OFFICIAL = 'kvv:21001:E:H'

if __name__ == '__main__':
    logger.info('Start analysing general SVM Classification for travel time')
    MLService().travel_time_class_svm(line_id=LINE, line_id_official=LINE_OFFICIAL)
