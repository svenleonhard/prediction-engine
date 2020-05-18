from machine_learning.model.ml_base import MLBase
from machine_learning.helper.time_difference import TimeDifference

class MLTravelTime(MLBase):

    name = 'travel_time'
    x_features = [
            'section',
            'planned_travel_time_class',
            'day_of_week',
            'current_delay',
            'daytime'
            # 'hour_real_time',
            # 'minute_real_time'
        ]
    y_feature = 'travel_time'
    non_numeric = [
        'station', 
        'target_station',
        'section'
    ]

    benchmark = 'planned_travel_time'

    def __init__(self, stop, target_stop):
        MLBase.__init__(self, stop, target_stop)

