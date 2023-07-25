import re
import hashlib
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pytz

from flask import Flask, render_template, request, session, redirect, url_for, jsonify

import utils.helper_functions as helper
import utils.mariadb_queries as maria_q
import utils.mongodb_queries as mongo_q

app = Flask(__name__)
# session data signed by server cryptographically
app.secret_key = "secret key"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        record = maria_q.authenticate(username, hashed_password)

        if record:
            session["loggedin"] = True
            session["id"] = record[0]
            session["username"] = record[4]
            session["isAdmin"] = record[6]
            if record[6]:
                return redirect(url_for("admin_home"))
            return redirect(url_for("home"))

        msg = "Incorrect credentials entered. Please check your username/password."
    return render_template("login.html", msg=msg)


@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if (
        request.method == "POST"
        and "name" in request.form
        and "email" in request.form
        and "area" in request.form
        and "username" in request.form
        and "password" in request.form
    ):
        name = request.form["name"]
        email = request.form["email"]
        area = request.form["area"]
        username = request.form["username"]
        password = request.form["password"]
        record = maria_q.regCheck(username)

        if record:
            msg = "Username/Account already exists !"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address !"
        elif not re.match(r"[A-Za-z0-9]+", username):
            msg = "Username must contain only characters and numbers !"
        elif not name or not email or not area or not username or not password:
            msg = "Please fill in all the fields!"
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            maria_q.register(name, email, area, username, hashed_password)
            msg = "You have successfully registered!"
            return redirect(url_for("login"))
    elif request.method == "POST":
        msg = "Please fill in all the fields!"
    return render_template("register.html", msg=msg)


@app.route("/admin_home")
def admin_home():
    record = maria_q.getAllUsers()
    return render_template(
        "admin_home.html",
        record=record,
        username=session["username"],
    )


@app.route('/delete_user', methods = ['POST'])
def delete_user():
    record_id = request.form.get('record_id')
    try:
        maria_q.deleteUser(record_id)
        return jsonify(success=True, message="User Deleted Successfully.")
    except Exception  as e:
        print(f"Error: {e}")
        return jsonify(success=False, message="Error deleting record")


@app.route("/admin_rewards")
def admin_rewards():
    record = maria_q.getAllRewards()
    return render_template(
        "admin_rewards.html",
        record = record,
    )


@app.route('/upload_image', methods = ['POST'])
def upload_image():
    if request.method == 'POST':
        reward_id = request.form.get('reward_id')
        image_file = request.files['image_file']
        if image_file:
            # Save the uploaded image name
            filename = image_file.filename
            file_path = "static/assets/rewards/" + filename
            image_file.save(file_path)
            maria_q.replaceImage(filename, reward_id)
    return redirect(url_for("admin_rewards"))


@app.route('/add_reward', methods=["GET", "POST"])
def add_reward():
    if request.method == "POST":
        name = request.form["name"]
        point_cost = request.form["point_cost"]
        stocks = request.form["stocks"]
        image_file = request.files['image_file']
        if name and point_cost and stocks and image_file:
            # Save the uploaded image name
            filename = image_file.filename
            file_path = "static/assets/rewards/" + filename
            image_file.save(file_path)
            maria_q.createReward(point_cost, name, filename, stocks)
        return redirect(url_for("admin_rewards"))
    return render_template("add_reward.html")


@app.route('/delete_reward', methods = ['POST'])
def delete_reward():
    record_id = request.form.get('record_id')
    try:
        maria_q.deleteReward(record_id)
        return jsonify(success=True, message="Reward Deleted Successfully.")
    except Exception  as e:
        print(f"Error: {e}")
        return jsonify(success=False, message="Error deleting record")


@app.route("/rewards")
def rewards():
    record = maria_q.getAllRewards()
    userPointsRecord = maria_q.getUserPoints()
    userPoints= userPointsRecord[0]
    return render_template(
        "rewards.html",
        record = record,
        userPoints = userPoints,
    )

@app.route('/redeem_reward', methods=['POST'])
def redeem_reward():
    if request.method == 'POST':
        reward_id = request.form.get('reward_id')
        record = maria_q.getRewardRecord(reward_id)
        point_cost = record[1]
        stock = record[4]
        userPointsRecord = maria_q.getUserPoints()
        userPoints= userPointsRecord[0]
        newUserPoints = userPoints - point_cost
        newStock = stock - 1
        maria_q.updateUserAfterRedemption(newUserPoints)
        maria_q.updateStock(newStock, reward_id)
        return jsonify(success=True, message="Redemption successful")
    return jsonify(success=False, message="Error processing redemption")

@app.route("/home")
def home():
    # user current points
    record = maria_q.getUserPoints()
    points = record[0]

    # recycles by month line chart
    record = maria_q.getRecyclesByMonth()
    recycles_by_month = []
    month_label = []
    for date, num in record:
        month_label.append(date.strftime("%b-%y"))
        recycles_by_month.append(num)

    # materials count bar chart
    record = maria_q.getMaterialCount()
    material_count = []
    material = []
    for mat, num in record:
        material.append(mat)
        material_count.append(num)

    # generate activity graph
    helper.generateGraph()
    graph_path = "static/assets/graphs/recentActivity.png"

    # reward transactions table
    record = maria_q.getRewardTransactions()
    transaction_dates = []
    reward_names = []
    claimed = []

    # Retrieve and append data to lists
    for date, id, claim in record:
        rewardName = maria_q.getRewardNameByRewardID(id)
        transaction_dates.append(date)
        reward_names.append(rewardName[0])
        if claim:
            claimed.append('Redeemed')
        else:
            claimed.append('Not Redeemed')

    # Create transaction_data list after appending data
    transaction_data = list(enumerate(zip(reward_names, transaction_dates, claimed), 1))
        
    return render_template(
        "home.html",
        username=session["username"],
        points=points,
        recycles_by_month=recycles_by_month,
        month_label=month_label,
        material=material,
        material_count=material_count,
        graph_path=graph_path,
        transaction_data=transaction_data,
    )


@app.route("/profile", methods=["GET", "POST"])
def profile():
    msg = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        area = request.form["area"]
        username = request.form["username"]
        password = request.form["password"]

        if name == "" or email == "" or area == "" or username == "":
            msg = "Please ensure all fields are filled in."
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address !"
        elif not re.match(r"[A-Za-z0-9]+", username):
            msg = "Username must contain only characters and numbers !"
        else:
            if password == "":
                maria_q.updateProfile(name, email, area, username)
                msg = "Profile Updated Successfully."
                session["username"] = username
            else:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                maria_q.updateProfileWPwd(name, email, area, username, hashed_password)
                msg = "Profile Updated Successfully."
                session["username"] = username

    details = maria_q.userProfile()

    return render_template("profile.html", msg=msg, details=details, isAdmin=session["isAdmin"])


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("q")  # Access the 'q' query parameter
    mquery = request.args.get("m")  # Access the 'm' query parameter

    if query or mquery:
        data = {"query": query}

        if query:
            data["record"] = maria_q.get_search("q", query)
        else:
            data["mrecord"] = maria_q.get_search("m", mquery)

        return render_template("qsearch.html", data=data)
    elif request.method == "POST":
        search_query = request.form.get("search_query")
        suggested_words = helper.get_suggestions(search_query)

        return render_template("search.html", suggested_words=suggested_words)
    else:
        return render_template("search.html")


@app.route("/get_suggestions", methods=["POST"])
def get_suggestions():
    search_query = request.json["search_query"]
    suggested_words = helper.get_suggestions(search_query)
    return jsonify({"suggested_words": suggested_words})


@app.route("/location")
def location():
    data = mongo_q.get_locations()
    user_location = maria_q.getUserLocation()

    return render_template("location.html", user_location=user_location, data=data)


@app.route("/scan", methods=["GET", "POST"])
def scan():
    queryBinID = request.args.get("qb")  # Access the 'qb' query parameter
    queryLocation = request.args.get("ql")  # Access the 'ql' query parameter

    if queryBinID and queryLocation:
        if request.method == "POST" and "materialType" in request.form:
            materialType = request.form["materialType"]
            f = request.files["fileInput"]
            if f.filename != "":
                fdir = "uploads/" + f.filename
                f.save(fdir)
                maria_q.recyle(queryBinID, fdir, materialType)
                msg = "You have successfully recycled!"
                return redirect(url_for("home"))
            else:
                maria_q.recyle(queryBinID, "", materialType)
                msg = "You have successfully recycled!"
                return redirect(url_for("home"))
        elif request.method == "POST":
            msg = "Please fill in all the fields!"
            return redirect(url_for("register"))

        return render_template(
            "form.html", queryBinID=queryBinID, queryLocation=queryLocation
        )
    else:
        return render_template("scan.html")


@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, ost="0.0.0.0", port=5000)
