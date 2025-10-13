import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error

class MYSQL_connect:
    # init function: a constructor -> when call this class the init runs first
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.config = {
                'user': user,
                'port': port,
                'password': password,
                'host': host,
        }
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
            print("---------------- Connected to MYSQL ----------------")

        except Error as e:
            raise Exception (f"Fail to connect to MYSQL: error {e}") from e

        return self.connection, self.cursor

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("---------------- MYSQL close connection ----------------")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
