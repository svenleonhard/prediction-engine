from database.database_weather import DatabaseWeather
from database.database_stop_weather import DatabaseStopWeather
from database.database import Database
from database.connection import Connection


class WeatherRepository():
    def __init__(self, session):
        self.session = session.session

    def find_weather_by_stop_id(self, stop_id):
        result = self.session.query(DatabaseStopWeather, DatabaseWeather) \
            .join(DatabaseStopWeather, DatabaseStopWeather.weatherID == DatabaseWeather.id) \
            .filter(DatabaseStopWeather.stopID == stop_id) \
            .first()

        if result:
            databaseWeather = result.DatabaseWeather
            return databaseWeather.to_weather_object()
        raise Exception('Empty Result')