from machine_learning.model.ml_base import MLBase

class MLTravelTimeClass(MLBase):

    name = 'travel_time'
    x_features = [
            'section',
            'delay_class',
            'day_of_week',
            'daytime',
            'planned_travel_time'
        ]
    y_feature = 'travel_time_class'
    non_numeric = [
        'station', 
        'target_station',
        'section'
    ]

    benchmark = 'planned_travel_time_class'

    def __init__(self, stop, target_stop):
        MLBase.__init__(self, stop, target_stop)

    def get_attributes_dict(self):
        return self.__dict__
