class NeoStop:
    def __init__(self, stop_id, stop_point_ref, stop_point_name,
                 timetabled_time, real_time, stop_seq_number,
                 operating_day_ref, journey_ref, line_ref, direction_ref,
                 pt_mode, submode, published_line_name, operator_ref,
                 route_description, origin_stop_point_ref, destination_text):
        self.stop_id = stop_id
        self.stop_point_ref = stop_point_ref
        self.stop_point_name = stop_point_name
        self.timetabled_time = timetabled_time
        self.real_time = real_time
        self.stop_seq_number = stop_seq_number
        self.operating_day_ref = operating_day_ref
        self.journey_ref = journey_ref
        self.line_ref = line_ref
        self.direction_ref = direction_ref
        self.pt_mode = pt_mode
        self.submode = submode
        self.published_line_name = published_line_name
        self.operator_ref = operator_ref
        self.route_description = route_description
        self.origin_stop_point_ref = origin_stop_point_ref
        self.destination_text = destination_text

    def delay(self):
        delay = self.real_time - self.timetabled_time
        return int(delay.total_seconds())