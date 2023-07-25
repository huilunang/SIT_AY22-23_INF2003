import os
import gridfs

from pymongo import MongoClient


class MongoDBConnManager:
    def __init__(self):
        self.client = MongoClient(
            host=os.environ["MONGO_HOST"],
            port=27017,
            username=os.environ["DB_USER"],
            password=os.environ["DB_PWD"],
            authSource=os.environ["DATABASE"],
        )

        self.gridfs = gridfs.GridFS(self.client.bloobin_db)

    def get_connection(self):
        return self.client

    def get_db(self):
        return self.client.bloobin_db

    def get_collection(self, collection):
        db = self.get_db()
        return db[collection]
    
    def get_file(self, id):
        # get the image via GridFs object
        self.gridfs.get(id)

    def set_file(self, filepath):
        with open(filepath, 'rb') as f:
            contents = f.read()

            # store/put the image via GridFs object & returns unique id
            return self.gridfs.put(contents)
