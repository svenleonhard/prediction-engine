from database.database_trip_section import DatabaseTripSection

from database.database import Database
from database.connection import Connection


class TripSectionRepository:
    def __init__(self, session):
        self.session = session.session

    def insert(self, trip_section):
        database_trip_section = DatabaseTripSection(
            trip_id=trip_section.trip_id,
            line_id=trip_section.line_id,
            station_from=trip_section.station_from.id,
            station_to=trip_section.station_to.id,
            travel_time=trip_section.travel_time)
        self.session.add(database_trip_section)
        self.session.commit()

    def trip_sections_for_line(self, line_id):
        trip_sections = self.session.query(DatabaseTripSection).filter_by(
            line_id=line_id).all()
        if trip_sections:
            return list(
                map(lambda trip_section: trip_section.to_trip_section_object(),
                    trip_sections))

    def travel_time(self, line_id, station_from):
        station_from_like = station_from.id + '%'

        trip_section = self.session.query(DatabaseTripSection) \
            .filter_by(line_id = line_id) \
            .filter(DatabaseTripSection.station_from.like(station_from_like)) \
            .first()
        if trip_section:
            return trip_section.to_trip_section_object()
