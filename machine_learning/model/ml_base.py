from machine_learning.helper.time_difference import TimeDifference

class MLBase(object):

    def __init__(self, stop, target_stop):
        self.station = stop.station_id.id
        # self.line = stop.line_id
        # self.journey = stop.journey_id
        self.current_delay = stop.delay()
        self.delay_class = stop.delay() / 60
        self.hour_real_time = stop.real_time.hour
        self.minute_real_time = stop.real_time.minute
        self.month_real_time = stop.real_time.month
        self.day_of_week = stop.real_time.weekday()
        self.hour_time_tabled_time = stop.time_tabled_time.hour
        self.minute_time_tabled_time = stop.time_tabled_time.minute
        self.month_time_tabled_time = stop.time_tabled_time.month
        self.target_station = target_stop.station_id.id
        self.daytime = self.calculate_daytime()

        self.planned_travel_time = TimeDifference.in_seconds(stop.time_tabled_time, target_stop.time_tabled_time)
        self.planned_travel_time_class =  self.encode_travel_time_class(self.planned_travel_time / 60)
        self.travel_time = TimeDifference.in_seconds(stop.real_time, target_stop.real_time)
        self.travel_time_minutes = self.travel_time / 60
        self.section = self.station + self.target_station

        self.travel_time_class = self.encode_travel_time_class(self.travel_time_minutes)


    def encode_travel_time_class(self, travel_time_minutes):
        if travel_time_minutes > 45:
            return int(10)
        if travel_time_minutes < 0:
            return int(0)
        return int(travel_time_minutes)

    def calculate_daytime(self):
        if self.hour_time_tabled_time < 6:
            return 0
        if self.hour_time_tabled_time >= 6 and self.hour_time_tabled_time < 9:
            return 1
        if self.hour_time_tabled_time >= 9 and self.hour_time_tabled_time < 12:
            return 2
        if self.hour_time_tabled_time >= 12 and self.hour_time_tabled_time < 14:
            return 3
        if self.hour_time_tabled_time >=14 and self.hour_time_tabled_time < 16:
            return 4
        if self.hour_time_tabled_time >=16 and self.hour_time_tabled_time < 18:
            return 4
        if self.hour_time_tabled_time < 24:
            return 5