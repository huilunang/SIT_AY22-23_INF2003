from database.mongodb_conn import MongoDBConnManager

mongo_db = MongoDBConnManager()

def get_locations():
    collection = mongo_db.get_collection("location")

    return [data for data in collection.find()]
