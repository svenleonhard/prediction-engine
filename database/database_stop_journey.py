import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.stop_journey import StopJourney

Base = declarative_base()
class DatabaseStopJourney(Base):

    __tablename__ = 'StopJourney'

    journeyID = sqlalchemy.Column(sqlalchemy.Integer)
    stopID	 = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    def to_stop_journey_object(self):
        return StopJourney(self.journeyID, self.stopID)