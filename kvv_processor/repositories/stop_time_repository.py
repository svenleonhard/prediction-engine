from database.database_stop_time import DatabaseStopTime

from database.database import Database
from database.connection import Connection

from sqlalchemy import distinct


class StopTimeRepository:
    def __init__(self, session):
        self.session = session.session

    def find_stops_by_trip_id(self, trip_id):
        stops = self.session.query(DatabaseStopTime).filter_by(
            trip_id=trip_id).all()
        return list(map(lambda stop: stop.to_stop_time_object(), stops))

    def number_of_stations(self, trip_id):
        number_of_stations = self.session.query(
            distinct(
                DatabaseStopTime.stop_id)).filter_by(trip_id=trip_id).count()
        return number_of_stations
