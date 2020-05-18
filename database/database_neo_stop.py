import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from kvv_processor.model.neo_stop import NeoStop

Base = declarative_base()
class DatabaseNeoStop(Base):

    __tablename__ = 'stops'

    stop_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    stop_point_ref = sqlalchemy.Column(sqlalchemy.String)
    stop_point_name = sqlalchemy.Column(sqlalchemy.String)
    timetabled_time = sqlalchemy.Column(sqlalchemy.DateTime)
    real_time = sqlalchemy.Column(sqlalchemy.DateTime)
    stop_seq_number = sqlalchemy.Column(sqlalchemy.Integer)
    operating_day_ref = sqlalchemy.Column(sqlalchemy.String)
    journey_ref = sqlalchemy.Column(sqlalchemy.String)
    line_ref = sqlalchemy.Column(sqlalchemy.String)
    direction_ref = sqlalchemy.Column(sqlalchemy.String)
    pt_mode = sqlalchemy.Column(sqlalchemy.String)
    submode = sqlalchemy.Column(sqlalchemy.String)
    published_line_name = sqlalchemy.Column(sqlalchemy.String)
    operator_ref = sqlalchemy.Column(sqlalchemy.String)
    route_description = sqlalchemy.Column(sqlalchemy.String)
    origin_stop_point_ref = sqlalchemy.Column(sqlalchemy.String)
    destination_text = sqlalchemy.Column(sqlalchemy.String)

    def to_neo_stop_object(self):
        return NeoStop(self.stop_id, self.stop_point_ref, self.stop_point_name,
                 self.timetabled_time, self.real_time, self.stop_seq_number,
                 self.operating_day_ref, self.journey_ref, self.line_ref, self.direction_ref,
                 self.pt_mode, self.submode, self.published_line_name, self.operator_ref,
                 self.route_description, self.origin_stop_point_ref, self.destination_text)