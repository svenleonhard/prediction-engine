class Trip:

    def __init__(self, trip_id, route_id, trip_headsign):
        self.trip_id = trip_id
        self.route_id = route_id
        self.trip_headsign = trip_headsign

    def __str__(self):
        return_string = []
        return_string.append('trip_section: ')
        return_string.append(str(self.trip_id))
        return_string.append(' on route: ')
        return_string.append(str(self.route_id))
        return_string.append(' with headsign : ')
        return_string.append(str(self.trip_headsign))

        return ''.join(return_string)
