import pymongo
import json
# from config import mongourl
from bson.objectid import ObjectId


with open('config.json') as f:
  config = json.load(f)




class database:
    def __init__(self):
        # we can take These on env var but are ignoring it here
        try:
            self._client = pymongo.MongoClient(config["MONGO_URI"])
            print("successfully connected to Atlas cluster : DB")

        except Exception as e:
            raise Exception(e)

        # try:
        #     self._client = pymongo.MongoClient(mongourl)
        # except Exception as e:
        #     raise Exception(e)
        self._db = self._client["testdb_4_green_deck"]
        self._coll = self._db["greendeck_data"]


    def insert (self,data:dict):

        return self._coll.insert_one(data)

    def get(self,limit=100):
        """ Get All Data from database"""
        
        return self._coll.find({}).limit(limit=limit)
    def find_one(self,_id):

        return self._coll.find_one({"_id": ObjectId(_id)})

    def find_one_and_delete(self,_id):
        """ find one data and delete"""
        return self._coll.find_one_and_delete({"_id":ObjectId(_id)})

    def find_one_and_update(self, old_data:dict ,new_data:dict):
        _newdata = {"$set": new_data}
        return self._coll.find_one_and_update(old_data, _newdata)

    def find(self,searchData:dict):
        """ searching in database"""

        return self._coll.find(searchData)


    def delete(self,del_data:dict)-> None:
        """ Deleting data from db """
        self._coll.delete_one(del_data)

    def update(self,old_data,new_data):
        _newdata = {"$set": new_data}
        return self._coll.update_one(old_data, _newdata)


