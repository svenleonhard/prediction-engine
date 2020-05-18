# from multiprocessing import Pool
import logging
from kvv_processor.journey_calculator import Journey_Calculator
from kvv_processor.kvv_processor_service import KvvProcessorService

logger = logging.getLogger(__name__)
LINE = 1

def calculate_journey(line):

    try:
        logger.info('Line: %s', str(line.line_id))
        journey_calculator = Journey_Calculator()
        journey_calculator.calculate_journeys_for_line(line.line_id)
    except Exception as e:
        logger.error(e)
        logger.error(line.line_id)


if __name__ == '__main__':
    lines = KvvProcessorService().list_of_lines()
    calculate_journey(lines[LINE - 1])
