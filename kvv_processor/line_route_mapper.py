import re, logging

logger = logging.getLogger(__name__)

class LineRouteMapper(object):

    def __init__(self, trip_repository, route_repository, stop_repository,
                 stop_time_repository):
        self.trip_repository = trip_repository
        self.route_repository = route_repository
        self.stop_repository = stop_repository
        self.stop_time_repository = stop_time_repository

    def map_line(self, line):
        logger.info('process line %s', line.line_id)

        route = self.extract_route_short_name(line.name)

        if not route:
            logger.info('line %s fits not to intended type', line.line_id)
            return

        trips = self.trips_for_line(line.destination, route)

        if trips:
            return self.check_trips(trips, route['route_short_name'],
                                    line.line_id)

    @classmethod
    def extract_route_short_name(self, line_name):
        line_types = ['Straßenbahn', 'S-Bahn', 'Nightliner']

        for line_type in line_types:
            check_type_result = re.sub(line_type + ' ', '', line_name)
            if not check_type_result == line_name:
                return {
                    'route_short_name': check_type_result,
                    'type': line_type
                }

    def trips_for_line(self, line_destination, route):

        if route['type'] != 'S-Bahn':
            trips = self.trip_repository.find_trips_by_trip_headsign(
                line_destination)
            if trips:
                return trips

        extracted_headsign = self.extract_headsign(line_destination,
                                                   route['route_short_name'])
        return self.trip_repository.find_trips_by_trip_headsign(
            extracted_headsign)

    @classmethod
    def extract_headsign(self, line_destination, route_short_name):
        return re.sub(route_short_name + ' ', '', line_destination)

    def check_trips(self, trips, route_short_name, line_id):
        number_of_stop_stations = self.stop_repository.number_of_stations(
            line_id)
        limitter = 5
        best_trip = trips[0]
        best_difference = self.compare_number_of_stations(
            trips[0], number_of_stop_stations)
        for trip in trips:
            if limitter == 0:
                break
            station_difference = self.compare_number_of_stations(
                trip, number_of_stop_stations)
            if station_difference == 0:
                route = self.route_repository.find_route_by_route_id(
                    trip.route_id)
                if str(route.route_short_name) == route_short_name:
                    return trip
            if best_difference > station_difference:
                best_trip = trip
                best_difference = station_difference
                limitter = limitter + 2
            limitter = limitter - 1
        if best_trip:
            return best_trip

    def compare_number_of_stations(self, trip, number_of_stop_stations):

        number_of_trip_stations = self.stop_time_repository.number_of_stations(
            trip.trip_id)

        return (number_of_stop_stations - number_of_trip_stations)**2