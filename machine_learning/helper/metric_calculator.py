class MetricCalculator(object):

    @classmethod
    def calculate(self, actual, expected, condition):
        counter = 0
        for i, item in enumerate(expected):
            if condition.evaluate(actual[i], item):
                counter = counter + 1
        return counter / len(expected)