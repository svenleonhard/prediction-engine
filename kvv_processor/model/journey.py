class Journey:

    def __init__(self, journey_id, stop_id):
        self.journey_id = journey_id
        self.stop_id = stop_id

    def to_string(self):
        journey_string = []
        journey_string.append('journey_id: ')
        journey_string.append(str(self.journey_id))
        journey_string.append(', stop_id: ')
        journey_string.append(str(self.stop_id))
        return ''.join(journey_string)