import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.stop_time import StopTime
from kvv_processor.model.station import Station

Base = declarative_base()
class DatabaseStopTime(Base):

    __tablename__ = 'KvvStopTimes'

    trip_id = sqlalchemy.Column(sqlalchemy.String(), primary_key=True)
    arrival_time = sqlalchemy.Column(sqlalchemy.String(), primary_key=True)
    departure_time = sqlalchemy.Column(sqlalchemy.String())
    stop_id = sqlalchemy.Column(sqlalchemy.String())
    stop_sequence = sqlalchemy.Column(sqlalchemy.String())
    stop_headsign = sqlalchemy.Column(sqlalchemy.String())
    pickup_type = sqlalchemy.Column(sqlalchemy.String())
    drop_off_type = sqlalchemy.Column(sqlalchemy.String())

    def to_stop_time_object(self):
        return StopTime(self.trip_id, self.arrival_time, self.departure_time, Station(self.stop_id))