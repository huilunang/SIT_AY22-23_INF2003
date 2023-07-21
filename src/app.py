from database.mongodb_conn import MongoDBConnManager

from flask import Flask, render_template, request, session, redirect, url_for, jsonify

import mariadb_queries as db

import re
import hashlib


app = Flask(__name__)

mongo_db = MongoDBConnManager()

# session data signed by server cryptographically
app.secret_key = "secret key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        record=db.authenticate(username, hashed_password)
        if record:
            session['loggedin']=True
            session['id']=record[0]
            session['username']=record[4]
            return redirect(url_for('home')) 
        else:
            msg='Incorrect credentials entered. Please check your username/password.'
    return render_template('login.html',msg=msg)

@app.route("/register", methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'area' in request.form and 'username' in request.form and 'password' in request.form:
        name = request.form['name']
        email = request.form['email']
        area = request.form['area']
        username = request.form['username']
        password = request.form['password']
        record = db.regCheck(username)
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
            db.register(name, email, area, username, hashed_password)
            msg = 'You have successfully registered!'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Please fill in all the fields!'
    return render_template('register.html', msg = msg)

@app.route("/home")
def home():
    # user current points
    record = db.getUserPoints()
    points = record[0]

    # recycles by month line chart
    record = db.getRecyclesByMonth()
    recycles_by_month = []
    month_label = []
    for date, num in record:
        month_label.append(date.strftime("%b-%y"))
        recycles_by_month.append(num)

    # materials count bar chart
    record = db.getMaterialCount()
    material_count = []
    material = []
    for mat, num in record:
        material.append(mat)
        material_count.append(num)

    return render_template('home.html', username=session['username'], points=points, recycles_by_month=recycles_by_month, month_label=month_label, material=material, material_count=material_count)

@app.route("/profile",methods=['GET','POST'])
def profile():
    msg=''
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
                db.updateProfile(name, email, area, username)
                msg = 'Profile Updated Successfully.'
                session['username']=username
            else:
                hashed_password=hashlib.sha256(password.encode()).hexdigest()
                db.updateProfileWPwd(name, email, area, username, hashed_password)
                msg = 'Profile Updated Successfully.'
                session['username']=username
    details=db.userProfile()
    return render_template('profile.html',msg=msg, details=details)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('q')  # Access the 'q' query parameter
    mquery = request.args.get('m')  # Access the 'q' query parameter
    # if query:
    #     conn = maria_db.get_conn()
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM info1 INNER JOIN info2 ON info1.id = info2.id WHERE info1.item = %s", (query,))
    #     record = cur.fetchone()

    #     return render_template('qsearch.html', query=query, record=record)
    # elif mquery:
    #     mrecord = []
    #     conn = maria_db.get_conn()
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM info1 INNER JOIN info2 ON info1.id = info2.id WHERE info1.type = %s", (mquery,))
    #     row_headers = [x[0] for x in cur.description]
    #     rv = cur.fetchall()

    #     for result in rv:
    #         mrecord.append(dict(zip(row_headers, result)))

    #     return render_template('qsearch.html', query=query, mrecord=mrecord)
    # else:
    #     if request.method == 'POST':
    #         search_query = request.form.get('search_query')
    #         suggested_words = retrieve_suggested_words_from_database(search_query)
    #         return render_template('search.html', suggested_words=suggested_words)
    #     return render_template('search.html')
    return render_template('search.html') # to remove

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
                db.recyle(queryBinID, fdir, materialType)
                msg = 'You have successfully recycled!'
                return redirect(url_for('home'))
            else:
                db.recyle(queryBinID, '', materialType)
                msg = 'You have successfully recycled!'
                return redirect(url_for('home'))
        elif request.method == 'POST':
            msg = 'Please fill in all the fields!'
            return redirect(url_for('register'))
        return render_template('form.html', queryBinID=queryBinID, queryLocation=queryLocation)
    else:
        return render_template('scan.html')

@app.route("/logout")
def logout():
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, ost='0.0.0.0', port=5000)