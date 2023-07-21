from database.mariadb_conn import MariaDBConnManager

from flask import session

maria_db = MariaDBConnManager()

def execute_sql_query(query, fetch_method, *args):
    conn = maria_db.get_conn()
    with conn.cursor() as cur:
        cur.execute(query, args)
        if fetch_method == 'one':
            return cur.fetchone()
        elif fetch_method == 'all':
            return cur.fetchall()
        elif fetch_method == 'many':
            return cur.fetchmany()
        elif fetch_method == '':
            conn.commit()

# login page
def authenticate(username, pwd):
    query = "SELECT * FROM Users WHERE username=%s AND password=%s"
    return execute_sql_query(query, 'one', username, pwd)

# register page
def regCheck(username):
    query = "SELECT * FROM Users WHERE username = %s"
    return execute_sql_query(query, 'one', username)

def register(name, email, area, username, pwd):
    query = "INSERT INTO Users (Name, Email, Area, Username, Password, isAdmin, Points) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    return execute_sql_query(query, '', name, email, area, username, pwd, False, 0)

# home page
def getUserPoints():
    query = "SELECT Points FROM Users WHERE UserID = %s"
    return execute_sql_query(query, 'one', session['id'])

def getRecyclesByMonth():
    query = "SELECT DATE(Datetime) AS recyDate, COUNT(*) AS NumRecords FROM Recycles WHERE UserID = %s GROUP BY recyDate ORDER BY recyDate"
    return execute_sql_query(query, 'all', session['id'])

def getMaterialCount():
    query = "SELECT MaterialType, COUNT(*) AS matCount FROM Recycles WHERE UserID = %s GROUP BY MaterialType"
    return execute_sql_query(query, 'all', session['id'])

# profile page
def updateProfile(name, email, area, username):
    query = "UPDATE Users SET name=%s, email=%s, area=%s, username=%s WHERE UserID = %s"
    return execute_sql_query(query, '', name, email, area, username, session['id'])

def updateProfileWPwd(name, email, area, username, password):
    query = "UPDATE Users SET name=%s, email=%s, area=%s, username=%s, password=%s WHERE UserID = %s"
    return execute_sql_query(query, '', name, email, area, username, password, session['id'])

def userProfile():
    query = "SELECT * FROM Users WHERE UserID=%s"
    return execute_sql_query(query, 'one', session['id'])

# scan page
def recyle(queryBinID, fdir, materialType):
    query = "INSERT INTO Recycles (RecycledID, BinID, Datetime, Image, MaterialType, UserID) VALUES (%s, %s, NOW(), %s, %s, %s)"
    return execute_sql_query(query, '', '', queryBinID, fdir, materialType, session['id'])

# search page