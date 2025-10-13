import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error

config = {
    'user': 'root',
    'port': 3306,
    'password': '123',
    'host': 'localhost',
    'database': 'github_data'
}
#
# try:
#     cnx = mysql.connector.connect(**config)
#
#     if cnx.is_connected():
#         print(f"Successfully connect to MYSQL database: {config['database']} ")
#
#         cursor = cnx.cursor()
#         cursor.execute("SELECT VERSION()")
#         db_version = cursor.fetchone()
#         print(f"Database version: {db_version}")
#         cursor.close()
#
# except mysql.connector.Error as e:
#     if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Access denied: check username or password")
#     elif e.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist.")
#     else:
#         print(f"Error: {e}")
# finally:
#     if 'cnx' in locals() and cnx.is_connected():
#         cnx.close()
#         print("MYSQL connection closed.")

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
