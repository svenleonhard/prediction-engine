from machine_learning.postprocessing.post_optimizer import PostOptimizer

import unittest
from unittest.mock import Mock

class TestPostOptimizer(unittest.TestCase):

    def setUp(self):
        self.post_optimizer = PostOptimizer()
        self.outputs = [25, 67, 92, -92]
        self.expected_optimization = [0, 60, 120, -120]
    
    def test_optimize(self):
        optimization = self.post_optimizer.optimize(self.outputs)
        self.assertEquals(optimization, self.expected_optimization)

if __name__ == '__main__':
    unittest.main()
