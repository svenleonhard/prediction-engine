from machine_learning.model.ml_base import MLBase

class MLDelay(MLBase):

    name = 'delay'
    x_features = [
            'station',
            'current_delay',
            'hour_real_time',
            'minute_real_time',
            'month_real_time',
            'hour_time_tabled_time',
            'minute_time_tabled_time',
            'month_time_tabled_time',
            'target_station',
            'day_of_week',
            'planned_delay'
        ]
    y_feature = 'delay'
    non_numeric = [
        'station', 
        'target_station'
    ]
    
    benchmark = 'planned_delay'

    def __init__(self, stop, target_stop):
        MLBase.__init__(self, stop, target_stop)
        self.planned_delay = 0 #stop.delay()
        self.delay = target_stop.delay() - stop.delay()