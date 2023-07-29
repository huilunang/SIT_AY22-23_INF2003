import base64

from database.mongodb_conn import MongoDBConnManager

from bson.objectid import ObjectId
from flask import session
import utils.helper_functions as helper

mongo_db = MongoDBConnManager()

def get_locations():
    collection = mongo_db.get_collection("location")

    return [data for data in collection.find()]

""" Tried to do for Pagination
    def get_locations_page(page_number, items_per_page):
    collection = mongo_db.get_collection("location")
    skip_count = (page_number - 1) * items_per_page

 # Get all data from the collection
    all_data = [data for data in collection.find()]

    # Extract recycling and e-bin data
    recycling = all_data[0]['features']
    ebin = all_data[1]['features']
    
    total_locations=0
    for entry in recycling:
        total_locations=total_locations+1

    for entry in ebin:
        total_locatiosn=total_locations+1

    #total_pages = (total_locations + items_per_page - 1) // items_per_page

    # Perform pagination on recycling and e-bin data
    paginated_recycling = recycling[skip_count:skip_count + items_per_page]
    paginated_ebin = ebin[skip_count:skip_count + items_per_page]
    
    return paginated_recycling, paginated_ebin,total_locations
 """
def get_suggestions(data, search_query):
    recycling=data[0]['features']
    ebin=data[1]['features']

    # Function to extract street names from recycling bin data
    def extract_recycling_street_names():
        for entry in recycling:
            yield entry["properties"]["description"]["value"]["ADDRESSSTREETNAME"]

    # Function to extract street names from e-bin data
    def extract_ebin_street_names():
        for entry in ebin:
            yield entry["properties"]["Description"]["ADDRESSSTREETNAME"]

    #Convert searcb query to lowercase 
    search_query_lower = search_query.lower()
    
    # Combine and sort the suggestions from both recycling and e-bin data
    suggested_words = set()
    for street_name in extract_recycling_street_names():
        if search_query_lower in street_name.lower():
            suggested_words.add(street_name)
    for street_name in extract_ebin_street_names():
        print(street_name)
        if search_query_lower in street_name.lower():
            suggested_words.add(street_name)

    # Sort the suggestions in alphabetical order and get the first 10
    sorted_suggestions = sorted(suggested_words)[:10]

    return sorted_suggestions


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
