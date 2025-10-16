from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class mongodb_connect:
    def __init__(self, mongo_uri, database):
        self.mongo_uri = mongo_uri
        self.database = database
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.mongo_uri)
            self.client.admin.command('ping')
            self.db = self.client[self.database]
            print(f" --------------- Successfully connected to MongoDB: {self.database} --------------")
        except ConnectionFailure as e:
            raise Exception(f"Fail to connect to MongoDB: {e}")

    def disconnect(self):
        if self.client:
            self.client.close()
        print("---------------- MYSQL close connection ----------------")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
