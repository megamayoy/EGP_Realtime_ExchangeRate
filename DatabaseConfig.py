from configparser import ConfigParser
import os
import psycopg2

class DatabaseConfig:

    """ configure postgresql database and store database configuration data """

    db_type = 'postgresql'
    db_configs_data = {}
    db_config_file = ""

    def __init__(self,db_config_file='DB_CONFIG.ini'):

        self.db_config_file = db_config_file
        parser = ConfigParser()
        parser.read(self.db_config_file)
        params = parser.items(self.db_type)
        for param in params:
            self.db_configs_data[param[0]] = param[1]

    def check_configs(self):

        """checks the correctness of the db configurations file path  and then
        checks if a connection to the database can be established """

        if not os.path.exists(self.db_config_file):
            print(self.db_config_file + "doesn't exist. please provide a valid config file path")
            return False

        else:

            try:
                connection = psycopg2.connect(**self.db_configs_data)

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print("please check database configuration data in DB_CONFIG.ini file")
                return False
            connection.close()

        print("we can connect to database successfully")
        return True

    def get_db_configs(self):
        return self.db_configs_data
