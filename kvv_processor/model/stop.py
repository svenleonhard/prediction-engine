from kvv_processor.helper.time_parser import TimeParser

class Stop:
    def __init__(self, stop_id, station_id, line_id, time_tabled_time,
                 real_time, journey_id):

        self.stop_id = stop_id
        self.station_id = station_id
        self.line_id = line_id
        self.time_tabled_time = self._string_check(time_tabled_time)
        self.real_time = self._string_check(real_time)
        self.journey_id = journey_id

    def delay(self):
        delay = self.real_time - self.time_tabled_time
        return int(delay.total_seconds())

    @classmethod
    def _string_check(self, to_check):
        if isinstance(to_check, str):
            return TimeParser().parse(to_check)
        return to_check
