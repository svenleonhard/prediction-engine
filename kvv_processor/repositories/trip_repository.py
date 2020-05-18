from database.database_trip import DatabaseTrip

from database.database import Database
from database.connection import Connection


class TripRepository:
    def __init__(self, session):
        self.session = session.session

    def find_trip_by_trip_headsign_fuzzy(self, trip_headsign):
        trip_headsign_search = '%{}%'.format(trip_headsign)
        database_trip = self.session.query(DatabaseTrip).filter(
            DatabaseTrip.trip_headsign.like(trip_headsign_search)).first()
        if database_trip:
            return database_trip.to_trip_object()

    def find_trips_by_trip_headsign(self, trip_headsign):
        trips = self.session.query(DatabaseTrip).filter_by(
            trip_headsign=trip_headsign).order_by(
                DatabaseTrip.route_id.desc()).all()
        if trips:
            return list(map(lambda trip: trip.to_trip_object(), trips))