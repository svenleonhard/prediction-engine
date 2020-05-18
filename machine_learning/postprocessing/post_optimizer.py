import numpy as np
import random

class PostOptimizer:

    def optimize(self, outputs):
        optimized = []
        for i, output in enumerate(outputs):
            optimized.append(self.round(output))
        return np.asarray(optimized)

    def round(self, value):
        mod = abs(value) % 60
        sign = 1
        if value < 0:
            sign = -1
        if mod < 32:
            value = value - mod * sign
        else:
            sub = 60 - mod
            value = value + sub * sign
        return value