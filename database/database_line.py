import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.line import Line

Base = declarative_base()
class DatabaseLine(Base):

    __tablename__ = 'Line'

    lineID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    destination = sqlalchemy.Column(sqlalchemy.String(length=150))

    def to_line_object(self):
        return Line(self.lineID, self.name, self.destination)