from database.mariadb_conn import MariaDBConnManager
from database.mongodb_conn import MongoDBConnManager

from flask import Flask, render_template, request, session, redirect, url_for, Response, jsonify

import re
import hashlib

import cv2
from pyzbar import pyzbar

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
    cur.execute("SELECT * FROM info1")

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
    if query:
        return render_template('qsearch.html', query=query)
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
    markers=[
    {
    'lat':0,
    'lon':0,
    'popup':'This is the middle of the map.'
        }
    ]

    json_data = []

    detection_result = mongo_db.get_collection("location")
    for data in detection_result.find():
        json_data.append(data)

    return render_template('location.html', username=session['username'],data=json_data, markers=markers)

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

@app.route("/register",methods=['GET','POST'])
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

def gen_frames():
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()

        if not success:
            break

        # Detect QR codes in the frame
        decoded_objs = pyzbar.decode(frame)

        for obj in decoded_objs:
            # Extract QR code data and display it
            qr_data = obj.data.decode('utf-8')
            print('QR Code:', qr_data)

        # Display the frame in the browser
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()

@app.route('/scan')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
