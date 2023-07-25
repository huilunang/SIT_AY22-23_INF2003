from database.mongodb_conn import MongoDBConnManager

from flask import session

mongo_db = MongoDBConnManager()

def get_locations():
    collection = mongo_db.get_collection("location")

    return [data for data in collection.find()]


def insert_detection(score, modelLabel, userLabel, fdir):
    collection = mongo_db.get_collection("detection_result")

    post = {
        "blob_imgId": "",
        "confidence_score": float(score),
        "model_labeled": modelLabel,
        "user_labeled": userLabel,
        "user_id": session["id"]
    }
    post_id = collection.insert_one(post).inserted_id

    image_id = mongo_db.set_file(fdir)
    collection.update_many(
        {"_id": post_id},
        { "$set" : { "blob_imgId": image_id } }
    )

    return str(image_id)