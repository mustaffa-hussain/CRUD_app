import pymongo
from config import mongourl
from bson.objectid import ObjectId
class database:
    def __init__(self):
        # we can take These on env var but are ignoring it here
        try:
            self._client = pymongo.MongoClient(mongourl)
        except Exception as e:
            raise Exception(e)
        self._db = self._client["greendeck"]
        self._col = self._db["ec_data"]


    def insert (self,data:dict):

        return self._col.insert_one(data)

    def get(self,limit=100):
        """ Get All Data from database"""
        
        return self._col.find({}).limit(limit=limit)
    def find_one(self,_id):

        return self._col.find_one({"_id": ObjectId(_id)})

    def find_one_and_delete(self,_id):
        """ find one data and delete"""
        return self._col.find_one_and_delete({"_id":ObjectId(_id)})

    def find_one_and_update(self, old_data:dict ,new_data:dict):
        _newdata = {"$set": new_data}
        return self._col.find_one_and_update(old_data, _newdata)

    def find(self,searchData:dict):
        """ searching in database"""

        return self._col.find(searchData)


    def delete(self,del_data:dict)-> None:
        """ Deleting data from db """
        self._col.delete_one(del_data)

    def update(self,old_data,new_data):
        _newdata = {"$set": new_data}
        return self._col.update_one(old_data, _newdata)


