import os
import mariadb


class MariaDBConnManager:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = mariadb.connect(
                user=os.environ['DB_USER'],
                password=os.environ['DB_PWD'],
                host=os.environ['MARIA_HOST'],
                port=3306,
                database=os.environ['DATABASE']
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            raise

    def get_conn(self):
        if not self.conn:
            self.connect()
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None
