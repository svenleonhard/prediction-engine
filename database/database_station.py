import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.station import Station

Base = declarative_base()
class DatabaseStation(Base):

    __tablename__ = 'Station'

    stationID = sqlalchemy.Column(sqlalchemy.String(length=20), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=80))
    
    def to_station_object(self):
        return Station(self.stationID, name=self.name)