from pymongo import MongoClient
from pprint import pprint
import getpass as gp
pw = gp.getpass()
username = "DJs"
password = pw
dbname = "djs-freeway"
uri = "mongodb+srv://" + username + ":" + password + \
    "@ccdm-project.f4c6t.mongodb.net/" + dbname + "?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)
    db = client.test
    print("Connected Successfully!!!")
except:
    print("Could not connect to db :( ")


mydb = client[dbname]

de_collection = mydb["freeway_detectors"]
lp_collection = mydb["freeway_loopdata"]

#Query 5 Find the path from Johnson Creek to I-205 NB at Columbia
i = 0
text = 'Johnson Cr NB'
print(i,":",text)
while text != 'I-205 NB at Columbia':
  qry5 = [ {'$match': {'locationtext': text}}, 
         {'$lookup': {
            'from': 'freeway_detectors', 
            'let': {'down': '$station.downstream', 
                'lanenum': '$lanenumber'}, 
            'pipeline': [{'$match': {'$expr': {
                            '$eq': ['$station.stationid', '$$down']}}},
                            {'$match': {'$expr': {'$eq': ['$lanenumber', '$$lanenum']}}}
            ], 
            'as': 'downstation'}},
            {'$limit': 1},
        {'$unwind': {'path': '$downstation'}},
        {'$project': {'downstation.locationtext': 1}}]
  cursor = de_collection.aggregate(qry5)
  result = list(cursor)
  i += 1
  for doc in result:
    text2 = doc["downstation"]
    text = text2["locationtext"]
    print(i,":",text)

