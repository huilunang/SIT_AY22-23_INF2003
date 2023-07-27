import utils.constant as const

from database.mariadb_conn import MariaDBConnManager

from flask import session

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
    INSERT INTO Users (Name, Email, Area, Username, Password, isAdmin, Points)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    result = maria_db.execute(query, "", name, email, area, username, pwd, False, 0)
    return result["result"]


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
    WHERE UserID = %
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


def getMaterialCount():
    query = """
    SELECT MaterialType, COUNT(*) AS matCount
    FROM Recycles WHERE UserID = %s AND Approved = 1
    GROUP BY MaterialType
    """

    result = maria_db.execute(query, "all", session["id"])
    return result["result"]


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
def get_search(query_param, value):
    if query_param == "q":
        query = """
        SELECT * FROM InfoRecyclables
        INNER JOIN
        InfoRecyclableTips ON InfoRecyclables.ItemID = InfoRecyclableTips.ItemID
        WHERE InfoRecyclables.Item = %s
        """

        fetch_method = "one"
        result = maria_db.execute(query, fetch_method, value)["result"]
    else:
        query = """
        SELECT * FROM InfoRecyclables
        INNER JOIN
        InfoRecyclableTips ON InfoRecyclables.ItemID = InfoRecyclableTips.ItemID
        WHERE InfoRecyclables.ItemType = %s
        """

        fetch_method = "all"
        result = maria_db.execute(query, fetch_method, value)

        row_headers = [x[0] for x in result["description"]]
        result = [dict(zip(row_headers, r)) for r in result["result"]]

    return result


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
