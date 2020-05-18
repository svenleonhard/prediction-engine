import logging
from kvv_processor.kvv_processor_service import KvvProcessorService
from kvv_processor.kvv_service import Kvv_Service

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    kvv_service = Kvv_Service()
    lines = kvv_service.list_of_lines()
    kvv_processor_service = KvvProcessorService()
    kvv_processor_service.calculate_travel_times(lines)
