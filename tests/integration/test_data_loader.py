from machine_learning.ioc_container import IoCContainer

import unittest, logging

logger = logging.getLogger(__name__)

class TestDataMap(unittest.TestCase):

    def setUp(self):
        self.data_loader = IoCContainer().data_loader_travel_time()

    def test_load(self):
        data_map = self.data_loader.load(line_id=18)
        self.assertGreater(len(data_map.x_train), 0)
        self.assertIsNotNone(data_map.df)
        
if __name__ == '__main__': 
    unittest.main()