import csv
import json
import pandas as pd 

# read in csv files into dataframes
df_de = pd.read_csv ("freeway_detectors.csv")
df_st = pd.read_csv ("freeway_stations.csv")
df_hw = pd.read_csv ("highways.csv")

#creates dictionary of highways
highways = {
    "3": {"highwayid": "3",
          "shortdirection": "N",
          "direction": "NORTH",
          "highwayname": "I-205"},
    "4": {"highwayid": "4",
          "shortdirection": "S",
          "direction": "SOUTH",
          "highwayname": "I-205"}
}
#create dictionary of stations
stations = {}
station = {}
#add to dictionary of stations from stations dataframe
for ind in df_st.index:
    #station = {}
    s_id = df_st.loc[ind, ["stationid"]]
    station["stationid"] = s_id
    station["upstream"] = df_st.loc[ind, ["upstream"]]
    station["downstream"] = df_st.loc[ind, ["downstream"]]
    station["stationclass"] = df_st.loc[ind, ["stationclass"]]
    station["numberlanes"] = df_st.loc[ind, ["numberlanes"]]
    station["latlon"] = df_st.loc[ind, ["latlon"]]
    station["length"] = df_st.loc[ind, ["length"]]
    stations[s_id] = station

#adds highway and station dictionaries for each detector
for ind in df_de.index:
    h_id = df_de.loc[ind, ["highwayid"]]
    df_de.loc[ind, ["highway"]] = highways[h_id]
    s_id = df_de.loc[ind, ["stationid"]]
    df_de.loc[ind, ["station"]] = stations[s_id]

#Save modifed dataframe to csv
df_de.to_csv("data/freeway_data.csv", index=False)