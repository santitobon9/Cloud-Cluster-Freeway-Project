import csv
import json
import pandas as pd 

# read in csv files into dataframes
df_de = pd.read_csv ("data/freeway_detectors.csv")
df_st = pd.read_csv ("data/freeway_stations.csv")
df_hw = pd.read_csv ("data/highways.csv")

#creates dictionary of highways
highways = {
    3: {
        "highwayid": "3",
        "shortdirection": "N",
        "direction": "NORTH",
        "highwayname": "I-205"
    },
    4: {
        "highwayid": "4",
        "shortdirection": "S",
        "direction": "SOUTH",
        "highwayname": "I-205"
    }
}
#print(highways[3])

stations = {}

#add to dictionary of stations from stations dataframe
for ind in df_st.index:
    station_id = int(df_st["stationid"][ind])
    station = { 
        station_id : {
            "stationid" : station_id,
            "upstream" : int(df_st["upstream"][ind]),
            "downstream" : int(df_st["downstream"][ind]),
            "stationclass" : int(df_st["stationclass"][ind]),
            "numberlanes" : int(df_st["numberlanes"][ind]),
            "latlon" : str(df_st["latlon"][ind]),
            "length" : float(df_st["length"][ind])
        }
    }
    stations.update(station)
    #print ("Station id:", s_id)
#print ("Stations:", stations)

detectors = []

#adds highway and station dictionaries for each detector
for ind in df_de.index:
    highway_id = int(df_de["highwayid"][ind])
    station_id = int(df_de["stationid"][ind])
    detector = {
        "detectorid" : int(df_de["detectorid"][ind]),
        "highway": highways[highway_id],
        "milepost": float(df_de["milepost"][ind]),
        "locationtext": str(df_de["locationtext"][ind]),
        "detectorclass": int(df_de["detectorclass"][ind]),
        "lanenumber": int(df_de["lanenumber"][ind]),
        "station": stations[station_id]
    }
    detectors.append(detector)


#Save detector list to json file
with open("detectors.json", "w") as detectors_file:
    json.dump(detectors, detectors_file, indent=4)
    

