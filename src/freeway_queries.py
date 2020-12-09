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
result1 = lp_collection.count_documents(
    {"speed": {"$lt": 5}})
print("Number of speeds < 5:", result1)
result2 = lp_collection.count_documents(
    {"speed": {"$gt": 80}})
print("Number of speeds > 80:", result2)

# Query 2: Find the total volume for the station Foster NB for Sept 15, 2011
result_q2 = mydb["freeway_loopdata"].aggregate([
    {
        '$lookup': {
            'from': 'freeway_detectors',
            'localField': 'detectorid',
            'foreignField': 'detectorid',
            'as': 'detectors'
        }
    }, {
        '$match': {
            'detectors.locationtext': 'Foster NB'
        }
    }, {
        '$match': {
            'starttime': {
                '$regex': '2011-09-15'
            }
        }
    }, {
        '$group': {
            '_id': 'None',
            'TotalVolume': {
                '$sum': '$volume'
            }
        }
    }
])

print("Query 2 Records:")
for record in result_q2:
    print(record)


# Query 3: Find travel time for station Foster NB for 5-Minute intervals for Sept 15, 2011.
# not complete
"""
result_q3 = mydb["freeway_loopdata"].aggregate([
    {
        "$match": {"starttime": {"$regex": '2011-09-15', "$options": 'i'}}
    },
    {
        "$lookup":
            {"from": "freeway_detectors", "localField": "detectorid",
                "foreignField": "detectorid", "as": "detector"
             }
    },
    {
        "$match": {"locationtext": {"$eq": 'Foster NB'}}
    }


])

for record in result_q3:
    print(record)
"""
# Query 6 update milepost at "Foster NB" from 18.1 -> 22.6
cursor6 = de_collection.find({"locationtext": {"$eq": 'Foster NB'}})
"""
print("Before query 6 update:")
for record in cursor6:
    print(record)
"""
query6 = de_collection.update_many({"locationtext": {"$eq": 'Foster NB'}}, {
    "$set": {"milepost": 22.6}})

cursor6 = de_collection.find({"locationtext": {"$eq": 'Foster NB'}})
print("After query 6 update:")
for record in cursor6:
    print(record)
"""
cursor = de_collection.find()
# print(cursor)
for record in cursor:
    print(record)
"""
