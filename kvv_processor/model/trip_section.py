class TripSection:
    def __init__(self, trip_id, line_id, station_from, station_to,
                 travel_time, trip_section_id=0):
        self.trip_section_id = trip_section_id
        self.trip_id = trip_id
        self.line_id = line_id
        self.station_from = station_from
        self.station_to = station_to
        self.travel_time = travel_time

    def __str__(self):
        return_string = []
        return_string.append('trip_section: ')
        return_string.append(str(self.trip_id))
        return_string.append(' from: ')
        return_string.append(str(self.station_from))
        return_string.append(' to : ')
        return_string.append(str(self.station_to))
        return_string.append(' in ')
        return_string.append(str(self.travel_time))

        return ''.join(return_string)