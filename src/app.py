from database.mariadb_conn import MariaDBConnManager
from database.mongodb_conn import MongoDBConnManager

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from utils.helper_functions import retrieve_suggested_words_from_database

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
    conn = maria_db.get_conn()
    cur = conn.cursor()

    # user current points
    query = "SELECT Points FROM Users WHERE UserID = %s"
    cur.execute(query, (session['id'],))
    record = cur.fetchone()
    points = record[0]

    # recycles by month line chart
    query = "SELECT DATE(Datetime) AS recyDate, COUNT(*) AS NumRecords FROM Recycles WHERE UserID = %s GROUP BY recyDate ORDER BY recyDate"
    cur.execute(query, (session['id'],))
    record = cur.fetchall()

    recycles_by_month = []
    month_label = []
    for date, num in record:
        month_label.append(date.strftime("%b-%y"))
        recycles_by_month.append(num)

    # materials count bar chart
    query = "SELECT MaterialType, COUNT(*) AS matCount FROM Recycles WHERE UserID = %s GROUP BY MaterialType"
    cur.execute(query, (session['id'],))
    record = cur.fetchall()

    material_count = []
    material = []
    for mat, num in record:
        material.append(mat)
        material_count.append(num)

    return render_template('home.html', username=session['username'], points=points, recycles_by_month=recycles_by_month, month_label=month_label, material=material, material_count=material_count)

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

@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    search_query = request.json['search_query']
    suggested_words = retrieve_suggested_words_from_database(search_query)
    return jsonify({'suggested_words': suggested_words})

@app.route("/location")
def location():
    conn = maria_db.get_conn()
    cur = conn.cursor()
    cur.execute('SELECT Area FROM Users WHERE UserID=%s', (session['id'],))
    user_location = cur.fetchone()[0]

    json_data = []

    location_result = mongo_db.get_collection("location")
    for data in location_result.find():
        json_data.append(data)

    return render_template('location.html', user_location=user_location, data=json_data)

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

@app.route("/profile",methods=['GET','POST'])
def profile():
    msg=''
    conn = maria_db.get_conn()
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        area = request.form['area']
        username = request.form['username']
        password = request.form['password']
        if name == "" or email=="" or area == "" or username == "":
            msg = 'Please ensure all fields are filled in.'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        else:
            if password == "":
                cur.execute('UPDATE Users SET name=%s, email=%s, area=%s, username=%s WHERE UserID = %s', (name, email, area, username,session['id']))
                conn.commit()
                msg = 'Profile Updated Successfully.'
                session['username']=username
            else:
                hashed_password=hashlib.sha256(password.encode()).hexdigest()
                cur.execute('UPDATE Users SET name=%s, email=%s, area=%s, username=%s, password=%s WHERE UserID = %s', (name, email, area, username, hashed_password,session['id']))
                conn.commit()
                msg = 'Profile Updated Successfully.'
                session['username']=username
    cur.execute('SELECT * FROM Users WHERE UserID=%s',(session['id'],))
    details=cur.fetchone()
    return render_template('profile.html',msg=msg, details=details)

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