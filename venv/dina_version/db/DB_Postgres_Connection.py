import psycopg2
class DB_Postgres_Connection:

    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            user='superup',
            password='12345678',
            dbname='superup'
        )
    def get_connection(self):
        return self.connection