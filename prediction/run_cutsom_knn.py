import logging
from context import machine_learning
from machine_learning.services.ml_service import MLService

logger = logging.getLogger(__name__)
LINE = 39
LINE_OFFICIAL = 'kvv:21003:E:H'

if __name__ == '__main__':
    logger.info('Start analysing custom KNN for travel time')
    MLService().custom_knn(official_line_id=LINE_OFFICIAL, line_id=LINE)
