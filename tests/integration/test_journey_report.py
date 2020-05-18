from kvv_processor.journey_reporter import JourneyReporter
from kvv_processor.kvv_processor_di_container import KvvProcessorDIContainer

import sys, numpy

import unittest, logging

logger = logging.getLogger(__name__)

class TestJourneyReporter(unittest.TestCase):

    def setUp(self):
        kvv_container = KvvProcessorDIContainer()
        self.journey_reporter = JourneyReporter(kvv_container.stop_repository(), kvv_container.station_repository())

    def test_(self):
        reported_journeys = self.journey_reporter.report_for(18)
        self.assertIsNotNone(reported_journeys)

if __name__ == '__main__': 
    unittest.main()
