import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.route import Route

Base = declarative_base()
class DatabaseRoute(Base):

    __tablename__ = 'KvvRoutes'

    route_id = sqlalchemy.Column(sqlalchemy.String(), primary_key=True)
    agency_id = sqlalchemy.Column(sqlalchemy.String())
    route_short_name = sqlalchemy.Column(sqlalchemy.String())
    route_long_name = sqlalchemy.Column(sqlalchemy.String())
    route_type = sqlalchemy.Column(sqlalchemy.String())
    route_color = sqlalchemy.Column(sqlalchemy.String())
    route_text_color = sqlalchemy.Column(sqlalchemy.String())

    def to_route_object(self):
        return Route(self.route_id, self.route_short_name, self.route_type)