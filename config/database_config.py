import os
from dotenv import load_dotenv
from dataclasses import dataclass

from databases.mongodb_connect import mongodb_connect


@dataclass
class MYSQL_config():
    host: str
    user: str
    password: str
    databases: str
    port: int

@dataclass
class Mongodb_config():
    uri: str
    databases: str

def get_db_config():
    load_dotenv()

    config = {
        "mysql": MYSQL_config(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            databases=os.getenv("MYSQL_DATABASE"),
            port=os.getenv("MYSQL_PORT")
        ),
        "mongodb": Mongodb_config(
            uri=os.getenv("MONGO_URI"),
            databases=os.getenv("MONGO_DATABASE")
        ),
        "redis": "",
        "postgresql": "",
        "elasticsearch": ""
    }

    return config
