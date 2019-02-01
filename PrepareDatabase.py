import DatabaseConfig as dc
import DatabaseInterface as dpi



db_config_obj = dc.DatabaseConfig()

# run database configuration  checks if errors occur , don't proceed
if not db_config_obj.check_configs():
    exit()

database_instance = dpi.DatabaseInterface()

# if table doesn't exist, create one
if database_instance.table_exists("egp_exchange_rates") is None:
    # create a table to store exchange rates
    print("creating a database table ..... ")

    # especially created for the application
    database_instance.create_table("""CREATE TABLE egp_exchange_rates
             (ID serial NOT NULL PRIMARY KEY, info json NOT NULL);""")






