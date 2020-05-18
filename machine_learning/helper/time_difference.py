class TimeDifference(object):

    @classmethod
    def in_seconds(self, departure_time, target_time):
        return (target_time - departure_time).total_seconds()
