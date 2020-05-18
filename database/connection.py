import yaml


class Connection:
    def __init__(self, database, schema):
        with open('database/credentials.yaml', 'r') as f:
            credentials_file = yaml.safe_load(f.read())
            credentials = credentials_file[database]

            self.user = credentials['user']
            self.password = credentials['password']
            self.host = credentials['host']
            self.database = credentials[schema]
            self.default_port = 3306

    def connection_string(self):
        connection = []

        connection.append('mysql+mysqlconnector://')
        connection.append(self.user)
        connection.append(':')
        connection.append(self.password)
        connection.append('@')
        connection.append(self.host)
        connection.append(':')
        connection.append(str(self.default_port))
        connection.append('/')
        connection.append(self.database)

        return ''.join(connection)