from machine_learning.helper.time_difference import TimeDifference

import unittest, datetime
from datetime import timedelta

class TestTimeDifference(unittest.TestCase):
    
    def test_in_seconds(self):
        target_time = datetime.datetime.now()
        departure_time = target_time - timedelta(seconds=120)
        time_difference = TimeDifference.in_seconds(departure_time, target_time)
        self.assertEquals(time_difference, 120)
        
if __name__ == '__main__':
    unittest.main()