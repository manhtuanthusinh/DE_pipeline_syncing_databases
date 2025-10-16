from databases.mongodb_connect import mongodb_connect
from databases.mysql_connect import MYSQL_connect
from config.database_config import get_db_config

def main(config):
    config_mysql = config["mysql"]
    with MYSQL_connect(config_mysql.host, config_mysql.port, config_mysql.user, config_mysql.password) as mysql_client:
        mysql_client.connect()

    config_mongodb = config["mongodb"]
    with mongodb_connect(config_mongodb.uri, config_mongodb.databases) as mongodb_client:
        mongodb_client.connect()

if __name__ == "__main__":
    config = get_db_config()
    main(config)
