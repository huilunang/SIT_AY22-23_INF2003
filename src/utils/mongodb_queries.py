import base64

from database.mongodb_conn import MongoDBConnManager

from bson.objectid import ObjectId
from flask import session

mongo_db = MongoDBConnManager()


def get_locations():
    collection = mongo_db.get_collection("location")

    return [data for data in collection.find()]


def get_detection(id):
    collection = mongo_db.get_collection("detection_result")

    detection = collection.find_one({"_id": ObjectId(id)})
    image = mongo_db.get_file(detection["image_id"]).read()
    encoded_image_data = base64.b64encode(image).decode("utf-8")

    return detection["model_labeled"], encoded_image_data


def insert_detection(score, modelLabel, fdir):
    collection = mongo_db.get_collection("detection_result")

    post = {
        "image_id": "",
        "confidence_score": float(score),
        "model_labeled": modelLabel,
        "user_id": session["id"],
    }
    post_id = collection.insert_one(post).inserted_id
    image_id = mongo_db.set_file(fdir)
    collection.update_one({"_id": post_id}, {"$set": {"image_id": image_id}})

    return str(post_id)


def set_material(detectionId, label):
    collection = mongo_db.get_collection("detection_result")

    collection.update_one(
        {"_id": ObjectId(detectionId)}, {"$set": {"confirmed_label": label}}
    )
