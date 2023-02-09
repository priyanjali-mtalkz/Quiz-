import pymongo
import json
from bson import json_util
from flask import jsonify
import time

class Schema():
    coll = []
    def __init__(self):
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017")
            db = client['Quiz']
            self.coll = db['UserDetails']
        except Exception as e:
            print("-----ERROR-----",e)
            
        print("Connection Successful")

    def user_getDetails(self):
        arr = []
        for x in self.coll.find():
            x['_id'] = str(x['_id'])
            arr.append(x)
        return json.dumps(arr, indent = 4, default= json_util.default)


    def user_add_details(self,data):
        #print(data)
        self.coll.insert_many(data)
        return jsonify({"Status" : "Insertion successful"})

    # def user_update_deatils(self,data,num):
    #     print(data)
    #     self.coll.update({"Mobile":num},{"$push" : {"user_answers" : data }})
    #     return jsonify({"Status":"Insertion successful"})