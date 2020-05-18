import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.station_neighbour import StationNeighbour

Base = declarative_base()
class DatabaseStationNeighbour(Base):

    __tablename__ = 'StationNeighbour'

    stationNeighbourId = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    stationID1 = sqlalchemy.Column(sqlalchemy.String(length=20))
    stationID2 = sqlalchemy.Column(sqlalchemy.String(length=20))
    lineID = sqlalchemy.Column(sqlalchemy.Integer)

    def to_station_neighbour_object(self):
        return StationNeighbour(self.stationNeighbourId, self.stationID1, self.stationID2, self.lineID)