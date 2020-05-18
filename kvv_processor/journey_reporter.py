from kvv_processor.journey_gruper import JourneyGrouper
from kvv_processor.model.journey_report import JourneyReport

import logging

logger = logging.getLogger(__name__)

class JourneyReporter(object):

    def __init__(self, stop_repository, station_repository):
        self.stop_repository = stop_repository
        self.station_repository = station_repository

    def report_for(self, line_id):
        stops = self.stop_repository.stops_for_line(line_id)
        journeys = JourneyGrouper.group(stops)
        reported_journeys = []
        for journey in journeys:
            stations = self.load_stop_info(journeys[journey])
            for i, stop in enumerate(journeys[journey]):
                logger.info(JourneyReport(stop, stations[i], journey))
                reported_journeys.append(JourneyReport(stop, stations[i], journey))
        return reported_journeys

    def load_stop_info(self, journey):
        stations = []
        for stop in journey:
            stations.append(self.station_repository.station_by_id(stop.station_id.id))
        return stations
