import psycopg2
import DatabaseConfig as dc

class DatabaseInterface:

    """a simple interface to execute PostgreSQL database operations especially creating tables
               and inserting records"""

    db_config = dc.DatabaseConfig()
    db_connection = None

    def __init__(self):

        #establishing a database connection

        try:
            self.db_connection = psycopg2.connect(**self.db_config.db_configs_data)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("can't connect to database. check database configuration data")


    def create_table(self,query_string):

        try:
            cursor = self.db_connection.cursor()
            cursor.execute(query_string)
            self.db_connection.commit()
            print("Table created successfully in PostgreSQL ")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while creating PostgreSQL table", error)



    def insert_record(self, insert_query,value):

            try:
                cursor = self.db_connection.cursor()
                cursor.execute(insert_query, (value,))
                self.db_connection.commit()
                count = cursor.rowcount
                print(count, "Record inserted successfully into table successfully")
            except (Exception, psycopg2.Error) as error:
                print("Failed to insert record")
                print(error)

            finally:
                cursor.close()


    def table_exists(self,table_name):

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""SELECT to_regclass(%s)""", ("public."+table_name,))
            flag = cursor.fetchone()[0]

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        return flag

    # close connection when object is destroyed
    def __del__(self):

        if self.db_connection is not None:
            self.db_connection.close()
