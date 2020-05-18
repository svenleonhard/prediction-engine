from kvv_processor.model.stop import Stop
from kvv_processor.model.station import Station

class NeoStopMapper:

    def map(self, neo_stops):
        stops = []
        for neo_stop in neo_stops:
            stops.append(self._create_stop(neo_stop))
        return stops

    def _create_stop(self, neo_stop):
        station = Station(neo_stop.stop_point_ref)
        line_id = sum(list(neo_stop.line_ref.encode('utf8'))) + 3200
        journey_id = neo_stop.journey_ref + neo_stop.operating_day_ref
        return Stop(neo_stop.stop_id, station, line_id, neo_stop.timetabled_time, neo_stop.real_time, journey_id)
