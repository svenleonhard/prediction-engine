from database.database_stop import DatabaseStop
from database.database_stop_journey import DatabaseStopJourney

from database.database import Database
from database.connection import Connection
from sqlalchemy import func, text, distinct


class StopRepository:
    def __init__(self, session):
        self.session = session.session

    def stops_by_delay(self, line_id, delay, station_id):
        stops = self.session.query(DatabaseStop, DatabaseStopJourney).filter_by(lineID = line_id) \
            .join(DatabaseStop, DatabaseStop.stopID == DatabaseStopJourney.stopID) \
            .filter_by(stationID = station_id) \
            .filter(func.timestampdiff(text('second'), DatabaseStop.timeTabledTime, DatabaseStop.realTime) == delay) \
            .all()
        return list(
            map(
                lambda stop: stop.DatabaseStop.to_stop_object(
                    stop.DatabaseStopJourney.journeyID), stops))

    def stops_by_delay_time_range(self, line_id, station_id, min_delay,
                                  max_delay):
        stops = self.session.query(DatabaseStop, DatabaseStopJourney).filter_by(lineID = line_id) \
            .join(DatabaseStop, DatabaseStop.stopID == DatabaseStopJourney.stopID) \
            .filter_by(stationID = station_id) \
            .filter(func.timestampdiff(text('second'), DatabaseStop.timeTabledTime, DatabaseStop.realTime) >= min_delay) \
            .filter(func.timestampdiff(text('second'), DatabaseStop.timeTabledTime, DatabaseStop.realTime) <= max_delay) \
            .all()
        return list(
            map(
                lambda stop: stop.DatabaseStop.to_stop_object(
                    stop.DatabaseStopJourney.journeyID), stops))

    def stop_by_id(self, stop_id):
        stop = self.session.query(DatabaseStop, DatabaseStopJourney) \
            .join(DatabaseStop, DatabaseStop.stopID == DatabaseStopJourney.stopID) \
            .filter_by(stopID = stop_id) \
            .first()

        if stop:
            return stop.DatabaseStop.to_stop_object(
                stop.DatabaseStopJourney.journeyID)

    def number_of_stations(self, line_id):
        number_of_stations = self.session.query(distinct(DatabaseStop.stationID)) \
            .filter_by(lineID = line_id) \
            .count()
        return number_of_stations

    def stops_for_line(self, line_id):
        stops = self.session.query(DatabaseStop, DatabaseStopJourney) \
            .join(DatabaseStop, DatabaseStop.stopID == DatabaseStopJourney.stopID) \
            .filter_by(lineID = line_id) \
            .order_by(DatabaseStop.timeTabledTime.asc()) \
            .all()
        return list(
            map(
                lambda stop: stop.DatabaseStop.to_stop_object(
                    stop.DatabaseStopJourney.journeyID), stops))


    def basic_stops_for_line(self, line_id, time):
        stops = self.session.query(DatabaseStop) \
            .filter(DatabaseStop.lineID == line_id) \
            .filter(DatabaseStop.timeTabledTime >= time) \
            .order_by(DatabaseStop.timeTabledTime.asc()) \
            .all()
        return list(
            map(
                lambda stop: stop.to_stop_object('0'), stops))

    def stop_for_journey(self, journey_id, station_id):
        result = self.session.query(DatabaseStopJourney, DatabaseStop) \
            .join(DatabaseStop, DatabaseStop.stopID == DatabaseStopJourney.stopID) \
            .filter(DatabaseStop.stationID == station_id) \
            .filter(DatabaseStopJourney.journeyID == journey_id) \
            .first()

        if result:
            databaseStop = result.DatabaseStop
            return databaseStop.to_stop_object(
                result.DatabaseStopJourney.journeyID)
        raise Exception('Empty Result')

    def stop_journey_id(self, stop_id):
        stop_journey = self.session.query(DatabaseStopJourney).filter_by(
            stopID=stop_id).first()
        if stop_journey:
            return stop_journey.journeyID
