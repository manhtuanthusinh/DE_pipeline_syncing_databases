import os
from dotenv import load_dotenv
from dataclasses import dataclass

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
        "mongo": "",
        "redis": "",
        "postgresql": "",
        "elasticsearch": ""
    }

    return config
