import os

from pymongo import MongoClient


class MongoDBConnManager:
    def __init__(self):
        self.client = MongoClient(host=os.environ['MONGO_HOST'],
                                  port=27017,
                                  username=os.environ['DB_USER'],
                                  password=os.environ['DB_PWD'],
                                  authSource=os.environ['DATABASE'])

    def get_connection(self):
        return self.client

    def get_db(self):
        return self.client.bloobin_db
    
    def get_collection(self, collection):
        db = self.get_db()
        return db[collection]
