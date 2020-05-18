from database.database_stop_journey import DatabaseStopJourney

class StopJourneyRepository:

    def __init__(self, session):
        self.session = session.session  
    
    def insert_journey(self, journey):
        database_stop_journey = DatabaseStopJourney(
            journeyID=journey.journey_id, stopID=journey.stop_id)
        self._insert(database_stop_journey)

    def _insert(self, database_object):
        self.session.add(database_object)
        self.session.commit()
