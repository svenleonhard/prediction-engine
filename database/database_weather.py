import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.weather import Weather

Base = declarative_base()
class DatabaseWeather(Base):

    __tablename__ = 'Weather'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    temp = sqlalchemy.Column(sqlalchemy.DECIMAL)
    humidity = sqlalchemy.Column(sqlalchemy.DECIMAL)
    pressure = sqlalchemy.Column(sqlalchemy.DECIMAL)
    wind = sqlalchemy.Column(sqlalchemy.DECIMAL)
    clouds = sqlalchemy.Column(sqlalchemy.DECIMAL)

    def to_weather_object(self):
        return Weather(self.id, self.temp, self.humidity, self.pressure, self.wind, self.clouds)