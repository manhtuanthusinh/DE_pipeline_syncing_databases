import os
from dotenv import load_dotenv
from dataclasses import dataclass


# get config
# host = os.getenv("MYSQL_HOST")
# port = os.getenv("MYSQL_PORT")
# user = os.getenv("MYSQL_USER")
# password = os.getenv("MYSQL_PASSWORD")
# database = os.getenv("MYSQL_DATABASE")

@dataclass
class MYSQL_config():
    host:str
    user:str
    password: str
    databases: str
    port: int

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
        "mongo": ""
    }
    return config

config = get_db_config()
print(config)