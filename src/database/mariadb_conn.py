import os
import mariadb
import pandas as pd

class MariaDBConnManager:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = mariadb.connect(
                user=os.environ["DB_USER"],
                password=os.environ["DB_PWD"],
                host=os.environ["MARIA_HOST"],
                port=3306,
                database=os.environ["DATABASE"],
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

    def execute(self, query, fetch_method, *args):
        conn = self.get_conn()

        with conn.cursor() as cur:
            cur.execute(query, args)

            data = {
                "description": cur.description,
            }

            if fetch_method == "one":
                data["result"] = cur.fetchone()
                return data
            elif fetch_method == "all":
                data["result"] = cur.fetchall()
                return data
            elif fetch_method == "many":
                data["result"] = cur.fetchmany()
                return data
            elif fetch_method == "":
                conn.commit()
    
    def executeForDataframe(self, query, args=None):
        conn = self.get_conn()
        if args is None:
            df = pd.read_sql_query(query, conn)
        else:
            df = pd.read_sql_query(query, conn, params=[args])
        return df
