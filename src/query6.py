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

#Query 6 update milepost at "Foster NB" from 18.1 -> 22.6
qry6 = de_collection.update_many({"locationtext": {"$eq":'Foster NB'}}, {"$set": {"milepost": 22.6}})

cursor = de_collection.find({"locationtext": {"$eq": 'Foster NB'}})
for record in cursor:
  print(record)
