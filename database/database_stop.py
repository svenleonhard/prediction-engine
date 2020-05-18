import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.stop import Stop
from kvv_processor.model.station import Station

Base = declarative_base()
class DatabaseStop(Base):

    __tablename__ = 'Stop'

    stopID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    stationID = sqlalchemy.Column(sqlalchemy.String(length=20))
    lineID = sqlalchemy.Column(sqlalchemy.Integer)
    timeTabledTime = sqlalchemy.Column(sqlalchemy.DateTime)
    realTime = sqlalchemy.Column(sqlalchemy.DateTime)

    def to_stop_object(self, journey_id):
        return Stop(self.stopID, Station(self.stationID), self.lineID, self.timeTabledTime, self.realTime, journey_id)