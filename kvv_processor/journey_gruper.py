from collections import defaultdict

class JourneyGrouper(object):

    @classmethod
    def group(self, stops):
        groups = defaultdict(list)
        
        for stop in stops:
            groups[stop.journey_id].append(stop)
        return groups