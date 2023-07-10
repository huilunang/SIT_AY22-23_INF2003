from database.mariadb_conn import MariaDBConnManager
from database.mongodb_conn import MongoDBConnManager

from flask import Flask, render_template, request, session, redirect, url_for, jsonify

import re
import hashlib


app = Flask(__name__)

maria_db = MariaDBConnManager()
mongo_db = MongoDBConnManager()

# session data signed by server cryptographically
app.secret_key = "secret key"

# TO BE DELETED
@app.route("/example")
def example_queries():
    json_data = []

    # mariadb example
    conn = maria_db.get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users")

    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()

    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # # mongodb example
    # detection_result = mongo_db.get_collection("location")
    # for data in detection_result.find():
    #     json_data.append(data)

    return render_template("example.html", data=json_data)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template('home.html', username=session['username'])

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('q')  # Access the 'q' query parameter
    mquery = request.args.get('m')  # Access the 'q' query parameter
    if query:
        conn = maria_db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM info1 INNER JOIN info2 ON info1.id = info2.id WHERE info1.item = %s", (query,))
        record = cur.fetchone()

        return render_template('qsearch.html', query=query, record=record)
    elif mquery:
        mrecord = []
        conn = maria_db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM info1 INNER JOIN info2 ON info1.id = info2.id WHERE info1.type = %s", (mquery,))
        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()

        for result in rv:
            mrecord.append(dict(zip(row_headers, result)))

        return render_template('qsearch.html', query=query, mrecord=mrecord)
    else:
        if request.method == 'POST':
            search_query = request.form.get('search_query')
            suggested_words = retrieve_suggested_words_from_database(search_query)
            return render_template('search.html', suggested_words=suggested_words)
        return render_template('search.html')

def retrieve_suggested_words_from_database(search_query):
    if len(search_query) >= 2:
        conn = maria_db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT item FROM info1 WHERE item LIKE %s ORDER BY item LIMIT 10", ('%' + search_query.replace(' ', '%') + '%',))
        suggested_words = [row[0] for row in cur.fetchall()]
        return suggested_words
    return False

@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    search_query = request.json['search_query']
    suggested_words = retrieve_suggested_words_from_database(search_query)
    return jsonify({'suggested_words': suggested_words})

@app.route("/location")
def location():
    json_data = []

    location_result = mongo_db.get_collection("location")
    for data in location_result.find():
        json_data.append(data)

    return render_template('location.html', username=session['username'],data=json_data)

@app.route("/login",methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        conn = maria_db.get_conn()
        cur = conn.cursor()
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        cur.execute('SELECT * FROM Users WHERE username=%s AND password=%s',(username,hashed_password))
        record=cur.fetchone()
        if record:
            session['loggedin']=True
            session['id']=record[0]
            session['username']=record[4]
            return redirect(url_for('home')) #create a home page
        else:
            msg='Incorrect credentials entered. Please check your username/password.'
    return render_template('login.html',msg=msg)

@app.route("/logout")
def logout():
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    return redirect(url_for('login'))

@app.route("/register", methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'area' in request.form and 'username' in request.form and 'password' in request.form:
        name = request.form['name']
        email = request.form['email']
        area = request.form['area']
        username = request.form['username']
        password = request.form['password']
        conn = maria_db.get_conn()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Users WHERE username = %s', (username, ))
        record = cur.fetchone()
        if record:
            msg = 'Username/Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not name or not email or not area or not username or not password:
            msg = 'Please fill in all the fields!'
        else:
            hashed_password=hashlib.sha256(password.encode()).hexdigest()
            cur.execute('INSERT INTO Users (Name, Email, Area, Username, Password, isAdmin, Points) VALUES (%s, %s, %s, %s, %s, %s, %s)', (name, email, area, username, hashed_password, False, 0))
            conn.commit()
            msg = 'You have successfully registered!'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill in all the fields!'
    return render_template('register.html', msg = msg)

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    queryBinID = request.args.get('qb')  # Access the 'qb' query parameter
    queryLocation = request.args.get('ql')  # Access the 'ql' query parameter
    if queryBinID and queryLocation:
        if request.method == 'POST' and 'materialType' in request.form:
            materialType = request.form['materialType']
            f = request.files['fileInput']
            if f.filename != '':
                fdir = "uploads/" + f.filename
                f.save(fdir)

                conn = maria_db.get_conn()
                cur = conn.cursor()
                cur.execute('INSERT INTO Recycles (RecycledID, BinID, Datetime, Image, MaterialType, UserID) VALUES (%s, %s, NOW(), %s, %s, %s)', ('', queryBinID, fdir, materialType, session['id']))
                conn.commit()
                msg = 'You have successfully recycled!'
                return redirect(url_for('home'))
            else:
                conn = maria_db.get_conn()
                cur = conn.cursor()
                cur.execute('INSERT INTO Recycles (RecycledID, BinID, Datetime, Image, MaterialType, UserID) VALUES (%s, %s, NOW(), %s, %s, %s)', ('', queryBinID, '', materialType, session['id']))
                conn.commit()
                msg = 'You have successfully recycled!'
                return redirect(url_for('home'))
        elif request.method == 'POST':
            msg = 'Please fill in all the fields!'
            return redirect(url_for('register'))
        return render_template('form.html', queryBinID=queryBinID, queryLocation=queryLocation)
    else:
        return render_template('scan.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
