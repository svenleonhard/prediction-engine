class KNNDelay(object):

    def __init__(self, delay, official_line_id, line_id, previous_station, target_station):
        self.delay = delay
        self.official_line_id = official_line_id
        self.line_id = line_id
        self.previous_station = previous_station
        self.target_station = target_station
