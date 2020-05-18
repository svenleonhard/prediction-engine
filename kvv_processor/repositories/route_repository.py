from database.database_route import DatabaseRoute
from database.database import Database
from database.connection import Connection


class RouteRepository():
    def __init__(self, session):
        self.session = session.session

    def find_route_by_route_id(self, route_id):
        route = self.session.query(DatabaseRoute).filter_by(
            route_id=route_id).first()
        if route:
            return route.to_route_object()

    def find_route_by_short_name(self, short_name):
        route = self.session.query(DatabaseRoute).filter_by(
            route_short_name=short_name).first()
        if route:
            return route.to_route_object()