from kvv_processor.kvv_processor_di_container import KvvProcessorDIContainer

class KvvProcessorService:

    def __init__(self):
        self.container = KvvProcessorDIContainer()
        self.neo_stop_repository = self.container.neo_stop_repository()
        self.neo_stop_mapper = self.container.neo_stop_mapper()
        self.stop_repository = self.container.stop_repository()
        self.trip_section_repository = self.container.trip_section_repository()
        self.line_repository = self.container.line_repository()
        self.stop_journey_repository = self.container.stop_journey_repository()
        self.weather_repository = self.container.weather_repository()

    def calculate_travel_times(self, lines):
        travel_time_calculator = self.container.travel_time_calculator()
        travel_time_calculator.calculate_travel_times(lines)

    def stops_for_line(self, line_id):
        if type(line_id) is int:
            return self.stop_repository.stops_for_line(line_id)
        
        return self.stops_for_line_from_neo(line_id)
    
    def neo_stops_for_line(self, line_ref):
        return self.neo_stop_repository.stops_for_line(line_ref)

    def trip_sections_by_line(self, line_id):
        return self.trip_section_repository.trip_sections_for_line(line_id)

    def stops_for_line_from_neo(self, line_ref):
        neo_stops = self.neo_stop_repository.stops_for_line(line_ref)
        stops = self.neo_stop_mapper.map(neo_stops)
        return stops

    def list_of_lines(self):
        return self.line_repository.list_of_lines()

    def insert_journey(self, journey):
        self.stop_journey_repository.insert_journey(journey)

    def basic_stops_for_line(self, line_id, time):
        return self.stop_repository.basic_stops_for_line(line_id, time)

    def find_weather_by_stop_id(self, stop_id):
        return self.weather_repository.find_weather_by_stop_id(stop_id)
