class RangeCondition(object):

    @classmethod
    def evaluate(self, actual, item):
        return item <= actual + 60 and item >= actual - 60