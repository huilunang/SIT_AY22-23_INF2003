from database.mariadb_conn import MariaDBConnManager

from flask import session

maria_db = MariaDBConnManager()


# login page
def authenticate(username, pwd):
    query = "SELECT * FROM Users WHERE username=%s AND password=%s"
    result = maria_db.execute(query, "one", username, pwd)
    return result["result"]


# register page
def regCheck(username):
    query = "SELECT * FROM Users WHERE username = %s"
    result = maria_db.execute(query, "one", username)
    return result["result"]


def register(name, email, area, username, pwd):
    query = "INSERT INTO Users (Name, Email, Area, Username, Password, isAdmin, Points) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    result = maria_db.execute(query, "", name, email, area, username, pwd, False, 0)
    return result["result"]


# home page
def getUserPoints():
    query = "SELECT Points FROM Users WHERE UserID = %s"
    result = maria_db.execute(query, "one", session["id"])
    return result["result"]


def getRecyclesByMonth():
    query = "SELECT DATE(Datetime) AS recyDate, COUNT(*) AS NumRecords FROM Recycles WHERE UserID = %s GROUP BY recyDate ORDER BY recyDate"
    result = maria_db.execute(query, "all", session["id"])
    return result["result"]


def getMaterialCount():
    query = "SELECT MaterialType, COUNT(*) AS matCount FROM Recycles WHERE UserID = %s GROUP BY MaterialType"
    result = maria_db.execute(query, "all", session["id"])
    return result["result"]


# profile page
def updateProfile(name, email, area, username):
    query = "UPDATE Users SET name=%s, email=%s, area=%s, username=%s WHERE UserID = %s"
    result = maria_db.execute(query, "", name, email, area, username, session["id"])
    return result["result"]


def updateProfileWPwd(name, email, area, username, password):
    query = "UPDATE Users SET name=%s, email=%s, area=%s, username=%s, password=%s WHERE UserID = %s"
    result = maria_db.execute(
        query, "", name, email, area, username, password, session["id"]
    )
    return result["result"]


def userProfile():
    query = "SELECT * FROM Users WHERE UserID=%s"
    result = maria_db.execute(query, "one", session["id"])
    return result["result"]


# scan page
def recyle(queryBinID, fdir, materialType):
    query = "INSERT INTO Recycles (RecycledID, BinID, Datetime, Image, MaterialType, UserID) VALUES (%s, %s, NOW(), %s, %s, %s)"
    result = maria_db.execute(
        query, "", "", queryBinID, fdir, materialType, session["id"]
    )
    return result["result"]


# search page
def get_search(query_param, value):
    if query_param == "q":
        query = "SELECT * FROM info1 INNER JOIN info2 ON info1.id = info2.id WHERE info1.item = %s"
        fetch_method = "one"
        result = maria_db.execute(query, fetch_method, value)["result"]
    else:
        query = "SELECT * FROM info1 INNER JOIN info2 ON info1.id = info2.id WHERE info1.type = %s"
        fetch_method = "all"
        result = maria_db.execute(query, fetch_method, value)

        row_headers = [x[0] for x in result["description"]]
        result = [dict(zip(row_headers, r)) for r in result["result"]]

    return result


def suggestion(search_query):
    query = "SELECT item FROM info1 WHERE item LIKE %s ORDER BY item LIMIT 10"
    arg = "%" + search_query.replace(" ", "%") + "%"
    result = maria_db.execute(query, "all", arg)
    return result["result"]

# location page
def getUserLocation():
    query = "SELECT Area FROM Users WHERE UserID=%s"
    result = maria_db.execute(query, "one", session['id'])
    return result
