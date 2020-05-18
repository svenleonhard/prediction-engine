from kvv_processor.neo_stop_mapper import NeoStopMapper
from kvv_processor.model.neo_stop import NeoStop
from kvv_processor.model.stop import Stop
from kvv_processor.model.station import Station
import unittest
from datetime import datetime

class TestNeoStopMapper(unittest.TestCase):

    def setUp(self):
        self.neo_stop_mapper = NeoStopMapper()
        datetime_format = '%Y-%m-%d %H:%M:%S'
        self.timetabled_time_1 = datetime.strptime('2020-02-05 12:32:00', datetime_format)
        real_time_1 = datetime.strptime('2020-02-05 12:33:00', datetime_format)
        neo_stop_1 = NeoStop(580, 'de:08212:84:3:3', 'Karlsruhe, Tivoli (Wendeschleife)',self.timetabled_time_1, real_time_1, 1, '2020-02-05T', 'kvv:21003:E:H:j20:251', 'kvv:21003:E:H', 'outward', 'tram', 'cityTram', 'Straßenbahn 3', 'kvv', 'Tivoli - Hbf Vorplatz - Mathystraße - Europaplatz - Neureut-Heide', 'de:08212:84:3:3', '3 Heide')
        timetabled_time_2 = datetime.strptime('2020-02-05 12:34:00', datetime_format)
        real_time_2 = datetime.strptime('2020-02-05 12:35:00', datetime_format)
        neo_stop_2 = NeoStop(685, 'de:08212:98:1:1', 'Karlsruhe Poststraße', timetabled_time_2, real_time_2, 1, '2020-02-05T', 'kvv:21003:E:H:j20:251', 'kvv:21003:E:H', 'outward', 'tram', 'cityTram', 'Straßenbahn 3', 'kvv', 'Tivoli - Hbf Vorplatz - Mathystraße - Europaplatz - Neureut-Heide', 'de:08212:84:3:3', '3 Heide')
        self.neo_stop_list = [neo_stop_1, neo_stop_2]

    def test_map(self):
        mapped_stops = self.neo_stop_mapper.map(self.neo_stop_list)
        self.assertIsInstance(mapped_stops[0], Stop)
        self.assertIsInstance(mapped_stops[1], Stop)

if __name__ == '__main__':
    unittest.main()