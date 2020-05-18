import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.trip_section import TripSection
from kvv_processor.model.station import Station

Base = declarative_base()
class DatabaseTripSection(Base):

    __tablename__ = 'TripSections'

    trip_section_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    trip_id = sqlalchemy.Column(sqlalchemy.String(length=50))
    line_id = sqlalchemy.Column(sqlalchemy.Integer)
    station_from = sqlalchemy.Column(sqlalchemy.String(length=20))
    station_to = sqlalchemy.Column(sqlalchemy.String(length=20))
    travel_time = sqlalchemy.Column(sqlalchemy.Integer)

    def to_trip_section_object(self):
        return TripSection(self.trip_id, self.line_id, Station(self.station_from), Station(self.station_to), self.travel_time, trip_section_id = self.trip_section_id)