import re

class Station:
    def __init__(self, station_id, name=''):
        self.id = station_id
        id_shorted_match = re.match('de:[0-9]*:[0-9]*',station_id)
        self.id_shorted = id_shorted_match.group(0)
        self.name = name

    def compare(self, station):

        station_id_1 = self.id.split(':')
        station_id_2 = station.id.split(':')

        min_length = min(len(station_id_1), len(station_id_2))

        for i in range(min_length):
            if station_id_1[i] != station_id_2[i]:
                return False

        return True
