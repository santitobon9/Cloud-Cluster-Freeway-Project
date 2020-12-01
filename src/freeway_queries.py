from pymongo import MongoClient
from pprint import pprint
import getpass as gp
pw = gp.getpass()
username = "DJs"
password = pw
dbname = "djs-freeway"
uri = "mongodb+srv://" + username + ":" + password + \
    "@ccdm-project.f4c6t.mongodb.net/" + dbname + "?retryWrites=true&w=majority"
#client = MongoClient()
#client = MongoClient(uri)
#db = client.test
try:
    client = MongoClient(uri)
    db = client.test
    print("Connected Successfully!!!")
except:
    print("Could not connect to db :( ")


mydb = client[dbname]

de_collection = mydb["freeway_detectors"]
lp_collection = mydb["freeway_loopdata"]

# Query 1: count the number of speeds < 5 mph and > 80 mph
result = lp_collection.count_documents(
    {"$or": [{"speed": {"$lt": 5}}, {"speed": {"$gt": 80}}]})
print("Query 1 count:", result)

# Query 2: Find the total volume for the station Foster NB for Sept 15, 2011
"""
result = mydb["freeway_loopdata"].aggregate(
    {"$lookup":
        {"from": "freeway_detectors", "localField": "detectorid",
            "foreignField": "detectorid", "as": "detector"
         }
     }
)
print("Query 2 Records:")
for record in result:
    print(record)
"""
"""
cursor = de_collection.find()
# print(cursor)
for record in cursor:
    print(record)
"""
