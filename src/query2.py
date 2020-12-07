from pymongo import MongoClient
from pprint import pprint
import getpass as gp
pw = gp.getpass()
username = "DJs"
password = pw
dbname = "djs-freeway"
uri = "mongodb+srv://" + username + ":" + password + \
    "@ccdm-project.f4c6t.mongodb.net/" + dbname + "?retryWrites=true&w=majority"
#print(uri)
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

#Query 2 Find the total volume for the station Foster NB for Sept 15, 2011
qry2 = [
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
  ]
cursor = lp_collection.aggregate(qry2)
result = list(cursor)

print("Query 2 results: ",result)
