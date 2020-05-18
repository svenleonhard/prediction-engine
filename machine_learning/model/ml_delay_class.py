from machine_learning.model.ml_base import MLBase
from machine_learning.helper.time_difference import TimeDifference

class MLDelayClass(MLBase):
    name = 'delay'
    x_features = [
        'station',
        'target_station',
        'day_of_week',
        'hour_real_time',
        'standard_prediction'
        ]
    y_feature = 'delay_changed'
    non_numeric = [
        'station', 
        'target_station',
        'section',
    ]
    benchmark='standard_prediction'

    def __init__(self, stop, target_stop):
        MLBase.__init__(self, stop, target_stop)
        self.standard_prediction = 0
        self.delay = target_stop.delay() - stop.delay()
        self.travel_time = TimeDifference.in_seconds(stop.real_time, target_stop.real_time)
        self.delay_changed = self.calculate_delay_changed(self.current_delay, self.delay)
    
    def calculate_delay_changed(self, current_delay, target_delay):
        delay_changed = target_delay - current_delay
        if delay_changed != 0:
            delay_changed = 1
        return delay_changed


        # 'station',
        # 'current_delay',
        # 'delay_class',
        # 'hour_real_time',
        # 'minute_real_time',
        # 'month_real_time',
        # 'day_of_week',
        # 'hour_time_tabled_time',
        # 'minute_time_tabled_time',
        # 'month_time_tabled_time',
        # 'target_station',
        # 'daytime',
        # 'standard_prediction'