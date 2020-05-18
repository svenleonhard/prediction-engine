import logging

logger = logging.getLogger(__name__)

class Validator:

    def check(self, trips):
        logger.info('Number of trips: %s', len(trips))
        valid_trips = []
        for trip in trips:
            logger.info('Number of stops in trip: %s', len(trip))
            valid = self.check_stops_of_trip(trip)
            if valid:
                valid_trips.append(trip)
        logger.info('Number of valid trips: %s', len(valid_trips))
        return valid_trips

    def check_stops_of_trip(self, stops):
        stations = {}
        for stop in stops:
            if stop.station_id.id in stations:
                return False
            stations[stop.station_id.id] = True
        return True
