from database.mariadb_conn import MariaDBConnManager

from flask import session
import datetime
import pytz

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


# admin home page 
def getAllUsers():
    query ="SELECT * FROM Users"
    result = maria_db.execute(query, "all")
    return result["result"]

def deleteUser(userID):
    query = "DELETE FROM Users WHERE UserID = %s"
    maria_db.execute(query, "", userID)


# admin rewards page 
def getAllRewards():
    query ="SELECT * FROM Rewards"
    result = maria_db.execute(query, "all")
    return result["result"]

def replaceImage(newFileName, rewardID):
    query = "UPDATE Rewards SET RewardImage = %s WHERE RewardID = %s"
    maria_db.execute(query,"", newFileName, rewardID)

def deleteReward(rewardID):
    query = "DELETE FROM Rewards WHERE RewardID = %s"
    maria_db.execute(query, "", rewardID)

def createReward(pointCost, name, fileName, stock):
    query = "INSERT INTO Rewards (PointCost, RewardName, RewardImage, Stock) VALUES (%s, %s, %s, %s)"
    maria_db.execute(query, "", pointCost, name, fileName, stock)

# rewards page
def getRewardRecord(rewardID):
    query = "SELECT * FROM Rewards WHERE RewardID = %s"
    result = maria_db.execute(query, "one", rewardID)
    return result["result"]

def updateUserAfterRedemption(newPoints):
    query = "UPDATE Users SET Points = %s WHERE UserID = %s"
    maria_db.execute(query, "", newPoints, session["id"])

def updateStock(newStock, rewardID):
    query = "UPDATE Rewards SET Stock = %s WHERE RewardID = %s"
    maria_db.execute(query, "", newStock, rewardID)

def getRewardTransactions():
    query = "SELECT TransactionDate, RewardID, Claimed FROM RewardTransactions WHERE UserID = %s"
    result = maria_db.execute(query, "all", session["id"])
    return result["result"]

def getRewardNameByRewardID(RewardID):
    query = "SELECT RewardName FROM Rewards WHERE RewardID = %s"
    result = maria_db.execute(query, "one", RewardID)
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

def getUserRecycleAcivity():
    end_date = datetime.datetime.now(pytz.timezone('Asia/Singapore')).date()
    start_date = end_date - datetime.timedelta(days=6)
    query = f'''SELECT DAYOFWEEK(DATE(Datetime)) AS DayOfWeek,
       DATE_FORMAT(Datetime, '%Y-%m-%d') AS Date,
       COUNT(*) AS TotalRecycled
        FROM Recycles
        WHERE UserID = %s
        AND DATE(Datetime) BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY Date
        ORDER BY Date;'''
    result = maria_db.executeForDataframe(query, session["id"])
    return result

def getRecycleActivity60days():
    end_date = datetime.datetime.now(pytz.timezone('Asia/Singapore')).date()
    start_date = end_date - datetime.timedelta(days=59) 
    query = f'''SELECT DATE(Datetime) AS Date,
    COUNT(*) AS TotalRecycled
    FROM Recycles
    WHERE DATE(Datetime) BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY Date
    ORDER BY Date
    '''
    result = maria_db.executeForDataframe(query)
    return result

def getRecycleMaterialActivity60days(materialType):
    end_date = datetime.datetime.now(pytz.timezone('Asia/Singapore')).date()
    start_date = end_date - datetime.timedelta(days=59) 
    query = f'''SELECT DATE(Datetime) AS Date,
    COUNT(*) AS TotalRecycled
    FROM Recycles
    WHERE MaterialType = '{materialType}'
    AND DATE(Datetime) BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY Date
    ORDER BY Date
    '''
    result = maria_db.executeForDataframe(query)
    return result


# profile page
def updateProfile(name, email, area, username):
    query = "UPDATE Users SET name=%s, email=%s, area=%s, username=%s WHERE UserID = %s"
    maria_db.execute(query, "", name, email, area, username, session["id"])


def updateProfileWPwd(name, email, area, username, password):
    query = "UPDATE Users SET name=%s, email=%s, area=%s, username=%s, password=%s WHERE UserID = %s"
    maria_db.execute(
        query, "", name, email, area, username, password, session["id"]
    )


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


