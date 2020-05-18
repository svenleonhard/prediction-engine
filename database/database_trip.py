import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.trip import Trip

Base = declarative_base()
class DatabaseTrip(Base):

    __tablename__ = 'KvvTrips'

    route_id = sqlalchemy.Column(sqlalchemy.String())
    service_id = sqlalchemy.Column(sqlalchemy.String())
    trip_id = sqlalchemy.Column(sqlalchemy.String(), primary_key=True)
    trip_headsign = sqlalchemy.Column(sqlalchemy.String())
    direction_id = sqlalchemy.Column(sqlalchemy.String())
    block_id = sqlalchemy.Column(sqlalchemy.String())
    bikes_allowed = sqlalchemy.Column(sqlalchemy.String())

    def to_trip_object(self):
        return Trip(self.trip_id, self.route_id, self.trip_headsign)