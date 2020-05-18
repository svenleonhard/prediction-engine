import sqlalchemy

class Database:

    def __init__(self, connection):

        self.engine = sqlalchemy.create_engine(connection.connection_string(), echo = False)

        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()