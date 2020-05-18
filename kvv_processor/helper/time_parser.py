from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class TimeParser(object):

    @classmethod
    def parse(self, time_string):
        first_two_digets = int(time_string[:2])

        if first_two_digets >= 24:
            time_delta = first_two_digets - 24
            time_string = str(time_delta) + time_string[2:]
            logger.warning(
                'time overflow (later then 23:59:59) in dataset, auto corrected it to %s',
                time_string)

        return datetime.strptime(time_string, '%H:%M:%S')