import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.weather import Weather

Base = declarative_base()
class DatabaseStopWeather(Base):

    __tablename__ = 'StopWeather'

    stopID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    weatherID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
