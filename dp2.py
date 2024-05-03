from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.gba4fj
# specify a collection
collection = db.dp2

directory = "data"

for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
        try:
            file_data = json.load(f)
            print(f,'successful')
            try:
                collection.insert_many(file_data)
            except Exception as e:
                print("import error")
        except Exception as e:
            print(e)
            print("error when loading", f)

 




