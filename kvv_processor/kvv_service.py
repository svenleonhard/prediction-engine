from database.database import Database
from database.connection import Connection
from database.database_line import DatabaseLine
from database.database_stop import DatabaseStop
from database.database_station_neighbour import DatabaseStationNeighbour
from database.database_stop_journey import DatabaseStopJourney

class Kvv_Service:
    def __init__(self):
        connection = Connection('local', 'history')
        self.session = Database(connection).session

    def all_stops_for_line(self, line_id):
        stops = self.session.query(DatabaseStop).filter_by(
            lineID=line_id).all()
        return list(map(lambda stop: stop.to_stop_object(), stops))

    def next_station_for_line(self, station_id, line_id):
        next_station = self.session.query(DatabaseStationNeighbour).filter_by(
            stationID1=station_id, lineID=line_id).first()
        if next_station:
            return next_station.to_station_neighbour_object()

    def stations_for_line(self, line):
        stations = self.session.query(DatabaseStationNeighbour).filter_by(
            lineID=line).all()
        return list(
            map(
                lambda station_neighbours: station_neighbours.
                to_station_neighbour_object(), stations))

    def planed_departure_times_for_station(self, station_id, line):
        stops_for_line_at_staion = self.session.query(DatabaseStop).filter_by(
            stationID=station_id, lineID=line).all()
        return list(
            map(lambda stop: stop.to_stop_object(), stops_for_line_at_staion))

    def list_of_lines(self):
        lines = self.session.query(DatabaseLine).order_by(
            DatabaseLine.lineID.asc()).all()
        return list(map(lambda line: line.to_line_object(), lines))

    def insert_journey(self, journey):
        database_stop_journey = DatabaseStopJourney(
            journeyID=journey.journey_id, stopID=journey.stop_id)
        self._insert(database_stop_journey)

    def _insert(self, database_object):
        self.session.add(database_object)
        self.session.commit()

    def find_stop_by_station_journey(self, target_station_id, journey_id):
        stop_by_station_journey = self.session.query(
            DatabaseStopJourney, DatabaseStop).join(DatabaseStop).filter_by(
                DatabaseStop.stopID == DatabaseStopJourney.stopID,
                stationID=target_station_id,
                journeyID=journey_id).first()
        if stop_by_station_journey:
            return stop_by_station_journey.to_stop_object()

    def find_journey_by_stop(self, stop_id):
        journey_by_stop = self.session.query(DatabaseStopJourney).filter_by(
            stopID=stop_id).first()
        if journey_by_stop:
            return journey_by_stop.to_stop_journey_object()

    @classmethod
    def delay(self, min_delay_minutes, line, station_id, limit):
        return 0