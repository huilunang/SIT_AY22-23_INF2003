import utils.constant as const

from database.mariadb_conn import MariaDBConnManager

from flask import session
import datetime
import pytz

maria_db = MariaDBConnManager()


# login page
def authenticate(username, pwd):
    query = """
    SELECT *
    FROM Users
    WHERE username=%s AND password=%s
    """

    result = maria_db.execute(query, "one", username, pwd)
    return result["result"]


# register page
def regCheck(username):
    query = """
    SELECT *
    FROM Users
    WHERE username = %s
    """

    result = maria_db.execute(query, "one", username)
    return result["result"]


def register(name, email, area, username, pwd):
    query = """
    INSERT INTO Users (UserID, Name, Email, Area, Username, Password, isAdmin, Points)
    VALUES (UUID(), %s, %s, %s, %s, %s, %s, %s)
    """

    maria_db.execute(query, "", name, email, area, username, pwd, False, 0)


# admin home page
def getAllUsers():
    query = """
    SELECT *
    FROM Users
    """

    result = maria_db.execute(query, "all")
    return result["result"]


def deleteUser(userID):
    query = """
    DELETE FROM Users
    WHERE UserID = %s
    """

    maria_db.execute(query, "", userID)


# admin rewards page
def getAllRewards():
    query = """
    SELECT *
    FROM Rewards
    """

    result = maria_db.execute(query, "all")
    return result["result"]


def replaceImage(newFileName, rewardID):
    query = """
    UPDATE Rewards
    SET RewardImage = %s
    WHERE RewardID = %s
    """

    maria_db.execute(query, "", newFileName, rewardID)


def deleteReward(rewardID):
    query = """
    DELETE FROM Rewards
    WHERE RewardID = %s
    """

    maria_db.execute(query, "", rewardID)


def createReward(pointCost, name, fileName, stock):
    query = """
    INSERT INTO Rewards (PointCost, RewardName, RewardImage, Stock)
    VALUES (%s, %s, %s, %s)
    """

    maria_db.execute(query, "", pointCost, name, fileName, stock)


# rewards page
def getRewardRecord(rewardID):
    query = """
    SELECT *
    FROM Rewards
    WHERE RewardID = %s
    """

    result = maria_db.execute(query, "one", rewardID)
    return result["result"]


def updateUserAfterRedemption(newPoints):
    query = """
    UPDATE Users
    SET Points = %s
    WHERE UserID = %s
    """

    maria_db.execute(query, "", newPoints, session["id"])


def updateStock(newStock, rewardID):
    query = """
    UPDATE Rewards
    SET Stock = %s
    WHERE RewardID = %s
    """

    maria_db.execute(query, "", newStock, rewardID)


def getTransactionInfo():
    query = """
    SELECT rt.TransactionID, r.RewardName, rt.TransactionDate, rt.Claimed 
    FROM Rewards r 
    JOIN RewardTransactions rt 
    ON r.RewardID = rt.RewardID
    WHERE rt.UserID = %s"""
    result = maria_db.execute(query, "all", session["id"])
    return result["result"]


def getRewardTransactions():
    query = "SELECT TransactionDate, RewardID, Claimed FROM RewardTransactions WHERE UserID = %s"
    result = maria_db.execute(query, "all", session["id"])
    return result["result"]


def updateRewardTransactions(TransactionID):
    query = "UPDATE RewardTransactions SET Claimed = true WHERE TransactionID = %s"
    maria_db.execute(query, "", TransactionID)


def getRewardNameByRewardID(RewardID):
    query = "SELECT RewardName FROM Rewards WHERE RewardID = %s"
    result = maria_db.execute(query, "one", RewardID)
    return result["result"]


def addTransaction(rewardID):
    currentDatetime = datetime.datetime.now(pytz.timezone("Asia/Singapore"))
    query = """
    INSERT INTO RewardTransactions (RewardID, UserID, TransactionDate, Claimed)
    VALUES (%s, %s, %s, %s)"""

    maria_db.execute(query, "", rewardID, session["id"], currentDatetime, False)


# approval page
def get_recycle():
    query = """
    SELECT RecycledID, UserID, Datetime, MaterialType, DetectionID
    FROM Recycles
    WHERE Approved = 0
    ORDER BY Datetime
    """

    result = maria_db.execute(query, "all")
    return result["result"]


def update_approval(approvalType, recycleId):
    query = """
    UPDATE Recycles
    SET Approved = %s
    WHERE RecycledID = %s
    """

    maria_db.execute(query, "", approvalType, recycleId)


# home page
def getUserPoints():
    query = """
    SELECT Points
    FROM Users
    WHERE UserID = %s
    """

    result = maria_db.execute(query, "one", session["id"])
    return result["result"]


def getDailyRecycles():
    currentDate = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    query = "SELECT COUNT(*) AS NumRecycles FROM Recycles WHERE DATE(Datetime) = %s"

    result = maria_db.execute(query, "one", currentDate)
    return result["result"]


def getUserDailyRecycles():
    currentDate = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    query = "SELECT COUNT(*) AS NumRecycles FROM Recycles WHERE DATE(Datetime) = %s AND UserID = %s"

    result = maria_db.execute(query, "one", currentDate, session["id"])
    return result["result"]


def getTotalRecycles():
    query = "SELECT COUNT(*) AS NumRecycles FROM Recycles"
    result = maria_db.execute(query, "one")
    return result["result"]


def getDailyRecycles():
    currentDate = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    query = "SELECT COUNT(*) AS NumRecycles FROM Recycles WHERE DATE(Datetime) = %s"

    result = maria_db.execute(query, "one", currentDate)
    return result["result"]


def getUserDailyRecycles():
    currentDate = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    query = "SELECT COUNT(*) AS NumRecycles FROM Recycles WHERE DATE(Datetime) = %s AND UserID = %s"

    result = maria_db.execute(query, "one", currentDate, session["id"])
    return result["result"]


def getTotalRecycles():
    query = "SELECT COUNT(*) AS NumRecycles FROM Recycles"
    result = maria_db.execute(query, "one")
    return result["result"]


def getRecyclesByMonth():
    query = """
    SELECT DATE(Datetime) AS recyDate, COUNT(*) AS NumRecords
    FROM Recycles
    WHERE UserID = %s AND Approved = 1
    GROUP BY recyDate
    ORDER BY recyDate
    """

    result = maria_db.execute(query, "all", session["id"])
    return result["result"]


def getBinCapacity():
    query = "SELECT Location, Capacity FROM Bins"

    result = maria_db.execute(query, "all")
    return result["result"]


def getMaterialCount():
    query = """
    SELECT MaterialType, COUNT(*) AS matCount
    FROM Recycles WHERE UserID = %s AND Approved = 1
    GROUP BY MaterialType
    """

    result = maria_db.execute(query, "all", session["id"])
    return result["result"]


def getTop5Recyclers():
    query = """
    SELECT u.Username, COUNT(r.RecycledID) AS NumRecycles
    FROM Users u
    LEFT JOIN Recycles r ON u.UserID = r.UserID
    GROUP BY u.UserID, u.Username
    ORDER BY NumRecycles DESC
    LIMIT 5
    """

    result = maria_db.execute(query, "all")
    return result["result"]


def getUserRecycleAcivity():
    end_date = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    start_date = end_date - datetime.timedelta(days=6)
    query = f"""SELECT DAYOFWEEK(DATE(Datetime)) AS DayOfWeek,
       DATE_FORMAT(Datetime, '%Y-%m-%d') AS Date,
       COUNT(*) AS TotalRecycled
        FROM Recycles
        WHERE UserID = %s
        AND DATE(Datetime) BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY Date
        ORDER BY Date;"""

    result = maria_db.executeForDataframe(query, session["id"])
    return result


def getRecycleActivity60days():
    end_date = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    start_date = end_date - datetime.timedelta(days=59)
    query = f"""
        SELECT DATE(Datetime) AS Date,
    COUNT(*) AS TotalRecycled
    FROM Recycles
    WHERE DATE(Datetime) BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY Date
    ORDER BY Date
    """

    result = maria_db.executeForDataframe(query)
    return result


def getRecycleMaterialActivity60days(materialType):
    end_date = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    start_date = end_date - datetime.timedelta(days=59)
    query = f"""
    SELECT DATE(Datetime) AS Date,
    COUNT(*) AS TotalRecycled
    FROM Recycles
    WHERE MaterialType = '{materialType}'
    AND DATE(Datetime) BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY Date
    ORDER BY Date
    """

    result = maria_db.executeForDataframe(query)
    return result


# profile page
def updateProfile(name, email, area, username):
    query = """
    UPDATE Users
    SET name=%s, email=%s, area=%s, username=%s
    WHERE UserID = %s
    """

    maria_db.execute(query, "", name, email, area, username, session["id"])


def updateProfileWPwd(name, email, area, username, password):
    query = """
    UPDATE Users
    SET name=%s, email=%s, area=%s, username=%s, password=%s
    WHERE UserID = %s
    """

    maria_db.execute(query, "", name, email, area, username, password, session["id"])


def userProfile():
    query = """
    SELECT *
    FROM Users
    WHERE UserID=%s
    """

    result = maria_db.execute(query, "one", session["id"])
    return result["result"]


# scan page
def recyle(queryBinID, detectionID, approved, materialType):
    query = """
    INSERT INTO Recycles (BinID, Datetime, DetectionID, Approved, MaterialType, UserID)
    VALUES (%s, NOW(), %s, %s, %s, %s)
    """

    maria_db.execute(
        query, "", queryBinID, detectionID, approved, materialType, session["id"]
    )


def add_points(userId):
    query = """
    UPDATE Users
    SET Points = Points + %s
    WHERE UserID = %s
    """

    maria_db.execute(query, "", const.RECYCLE_POINTS, userId)


# search page
def get_search(query_param, value, offset, limit):
    if query_param == "q":
        query = """
        SELECT * FROM InfoRecyclables
        INNER JOIN
        InfoRecyclableTips ON InfoRecyclables.ItemID = InfoRecyclableTips.ItemID
        WHERE InfoRecyclables.Item LIKE %s
        LIMIT %s OFFSET %s
        """

        fetch_method = "all"
        result = maria_db.execute(query, fetch_method, "%" + value + "%", limit, offset)

        row_headers = [x[0] for x in result["description"]]
        result = [dict(zip(row_headers, r)) for r in result["result"]]
    else:
        query = """
        SELECT * FROM InfoRecyclables
        INNER JOIN
        InfoRecyclableTips ON InfoRecyclables.ItemID = InfoRecyclableTips.ItemID
        WHERE InfoRecyclables.ItemType = %s
        LIMIT %s OFFSET %s
        """

        fetch_method = "all"
        result = maria_db.execute(query, fetch_method, value, limit, offset)

        row_headers = [x[0] for x in result["description"]]
        result = [dict(zip(row_headers, r)) for r in result["result"]]
    return result


def get_material_stats(value):
    query = """
    SELECT * FROM InfoStats
    WHERE InfoStats.WasteType = %s 
    ORDER BY InfoStats.Year ASC
    """

    fetch_method = "all"
    result = maria_db.execute(query, fetch_method, value)

    row_headers = [x[0] for x in result["description"]]
    result = [dict(zip(row_headers, r)) for r in result["result"]]
    # Check if result is empty
    if not result:
        # Return None if empty
        return None
    return result


def get_total_number_of_items(query_param, value):
    if query_param == "q":
        query = """
            SELECT COUNT(*) FROM InfoRecyclables
            WHERE InfoRecyclables.Item LIKE %s
            """
        fetch_method = "one"  # Single result with the count
        result = maria_db.execute(query, fetch_method, "%" + value + "%")
    else:
        query = """
            SELECT COUNT(*) FROM InfoRecyclables
            WHERE InfoRecyclables.ItemType = %s
        """
        fetch_method = "one"  # Single result with the count
        result = maria_db.execute(query, fetch_method, value)
    total_items = result["result"][0]  # Access the count directly
    return total_items


def suggestion(search_query):
    query = """
    SELECT Item
    FROM InfoRecyclables
    WHERE Item LIKE %s
    ORDER BY Item
    LIMIT 10
    """

    arg = "%" + search_query.replace(" ", "%") + "%"
    result = maria_db.execute(query, "all", arg)
    return result["result"]


# location page
def getUserLocation():
    query = """
    SELECT Area
    FROM Users
    WHERE UserID=%s
    """

    result = maria_db.execute(query, "one", session["id"])
    return result
