from database.database_neo_stop import DatabaseNeoStop

class NeoStopRepository:

    def __init__(self, session):
        self.session = session.session

    def stops_for_line(self, line_ref):
        stops = self.session.query(DatabaseNeoStop) \
            .filter(DatabaseNeoStop.line_ref == line_ref) \
            .filter(DatabaseNeoStop.direction_ref == 'outward') \
            .order_by(DatabaseNeoStop.timetabled_time.asc()) \
            .all()
        return list(
            map(
                lambda stop: stop.to_neo_stop_object(), stops))
