import os
import mariadb

from flask import Flask, render_template


app = Flask(__name__)


# TO BE DELETED
@app.route("/example")
def example_queries():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user=os.environ['DB_USER'],
            password=os.environ['DB_PWD'],
            host=os.environ['MARIA_HOST'],
            port=3306,
            database=os.environ['DB']
        )

        cur = conn.cursor()
        cur.execute("SELECT * FROM Users")

        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()

        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    return render_template("example.html", data=json_data)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)