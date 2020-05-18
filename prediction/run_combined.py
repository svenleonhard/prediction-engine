import logging
from context import machine_learning
from machine_learning.services.ml_service import MLService

logger = logging.getLogger(__name__)
LINE = 18
LINE_OFFICIAL = 'kvv:21001:E:H'

if __name__ == '__main__':
    logger.info('Start analysing combiend prediction for travel time')
    MLService().combined_prediction(line_id=LINE, line_id_official=LINE_OFFICIAL)
