from database.database_station import DatabaseStation

from database.database import Database
from database.connection import Connection
from sqlalchemy import func, text, distinct


class StationRepository:
    def __init__(self, session):
        self.session = session.session

    def station_by_id(self, station_id):
        station = self.session.query(DatabaseStation).filter_by(
            stationID=station_id).first()
        if station:
            return station.to_station_object()
