import csv
import pandas as pd 

# read in csv files into dataframes
df_de = pd.read_csv ("data/freeway_detectors.csv")
df_st = pd.read_csv ("data/freeway_stations.csv")
df_hw = pd.read_csv ("data/highways.csv")

#creates dictionary of highways
highways = {
    3: {"highwayid": "3",
          "shortdirection": "N",
          "direction": "NORTH",
          "highwayname": "I-205"},
    4: {"highwayid": "4",
          "shortdirection": "S",
          "direction": "SOUTH",
          "highwayname": "I-205"}
}
#print(highways[3])

stations = {}

#add to dictionary of stations from stations dataframe
for ind in df_st.index:
    station = {}
    s_id = df_st["stationid"][ind]
    station["stationid"] = s_id
    station["upstream"] = df_st["upstream"][ind]
    station["downstream"] = df_st["downstream"][ind]
    station["stationclass"] = df_st["stationclass"][ind]
    station["numberlanes"] = df_st["numberlanes"][ind]
    station["latlon"] = df_st["latlon"][ind]
    station["length"] = df_st["length"][ind]
    stations[s_id] = station
    #print ("Station id:", s_id)
#print ("Stations:", stations)

highway_list = list()
station_list = list()

#adds highway and station dictionaries for each detector
for ind in df_de.index:
    h_id = df_de["highwayid"][ind]
    #print ("Highway:", highways[h_id])
    highway_list.append(highways[h_id])
    s_id = df_de["stationid"][ind]
    station_list.append(stations[s_id])

#adds new highway and station columns
df_de["highway"] = highway_list
df_de["station"] = station_list
#print(df_de['highway'])
#print(df_de['station'])

#Save modifed dataframe to csv
df_de.to_csv("data/freeway_data.csv", index=False)