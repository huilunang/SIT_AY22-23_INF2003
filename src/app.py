from database.mariadb_conn import MariaDBConnManager
from database.mongodb_conn import MongoDBConnManager

from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)

maria_db = MariaDBConnManager()
mongo_db = MongoDBConnManager()

# session data signed by server cryptographically
app.secret_key = "secret key"

# mariadb
conn = maria_db.get_conn()
cur = conn.cursor()

# TO BE DELETED
@app.route("/example")
def example_queries():
    json_data = []

    # mariadb example
    conn = maria_db.get_conn()
    cur = conn.cur()
    cur.execute("SELECT * FROM Users")

    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()

    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # mongodb example
    detection_result = mongo_db.get_collection("detection_result")
    for data in detection_result.find():
        json_data.append(data)

    return render_template("example.html", data=json_data)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template('home.html', username=session['username'])

@app.route("/register")
def reg():
    return "Registration account"

@app.route("/login",methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        cur.execute('SELECT * FROM Users WHERE username=%s AND password=%s',(username,password))
        record=cur.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('home')) #create a home page
        else:
            msg='Incorrect credentials entered. Please check your username/password.'
    return render_template('login.html',msg=msg)

@app.route("/logout")
def logout():
    session.pop('loggedin',None)
    session.pop('username',None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
