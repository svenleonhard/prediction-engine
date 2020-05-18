from database.database_line import DatabaseLine

class LineRepository:

    def __init__(self, session):
        self.session = session.session  
    
    def list_of_lines(self):
        lines = self.session.query(DatabaseLine).order_by(
            DatabaseLine.lineID.asc()).all()
        return list(map(lambda line: line.to_line_object(), lines))
