from databases.mysql_connect import MYSQL_connect
from config.database_config import get_db_config

def main(config):
    with MYSQL_connect(config["mysql"].host, config["mysql"].port, config["mysql"].user, config["mysql"].password) as mysql_client:
        mysql_client.connect()

if __name__ == "__main__":
    config = get_db_config()
    main(config)