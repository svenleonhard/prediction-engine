class JourneyReport(object):

    def __init__(self, stop, station, journey):
        self.journey = journey
        self.stop_id = stop.stop_id
        self.time_tabled_time = stop.time_tabled_time
        self.station_name = station.name
        self.station_id = station.id

    def __str__(self):
     return ', '.join([
         self.journey,
         str(self.stop_id),
         str(self.time_tabled_time),
         self.station_name,
         str(self.station_id)
     ])
