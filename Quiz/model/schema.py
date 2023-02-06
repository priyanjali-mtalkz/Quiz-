import pymongo
import json

class Schema():

    def __init__(self):
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017")
            db = client['Quiz']
            self.coll = db['Questions']
        except Exception as e:
            print("-----ERROR-----",e)
            
        print("Connection Successful")
    def user_signup(self):
        for x in self.coll.find():
            x['_id'] = str(x['_id'])
            return (x)