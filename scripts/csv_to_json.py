__author__ = 'dhanannjay.deo'

"""
Goal is to interprete the csv files for constituency map, and the election results,
and write back in geo-json format which will be easy to read by webapp

{"type":"Feature","id":"01","properties":{"name":"Alabama","density":94.65},"geometry":{"type":"Polygon","coordinates":[[[-87.359296,35.00118], .. ]]}},

"""
import json
import csv
import sys
import os
rootpath = os.path.abspath(os.path.dirname(__file__))
from Polygon.Utils import reducePoints

decimation_factor = 0.2
reader = csv.reader(open(rootpath + "/../data/india_spatial.csv"), skipinitialspace=True)

count = -1
geojson = {"type":"FeatureCollection",
           "features": []}


def new_feature():
    return {"type" : "Feature", "id" : "" , "properties" : { "name": "", "state" : ""},
                   "geometry" : {"type" : "Polygon", "points" : []}}

current_feature = new_feature()
const_count = 0
for r in reader:
    # Skip first row of titles
    count = count + 1
    if count == 0:
        # print "Skip"
        continue

    # Find out if we are dealing with the same constituency
    if r[7] != current_feature["properties"]["name"]:
        # Not so create a new feature and insert current feature

        if current_feature["properties"]["name"] != "":
            current_feature["geometry"]["coordinates"] = [ reducePoints(current_feature["geometry"]["points"], int(len(current_feature["geometry"]["points"]) * decimation_factor))]
            del current_feature["geometry"]["points"]
            geojson["features"].append(current_feature)
            print "Feature Saved: ", current_feature["properties"]["name"], current_feature["properties"]["state"], ",", len(current_feature["geometry"]["coordinates"]), " Coordinates."
            # if len(geojson["features"]) > 3:
            #     break
                            # Create new featire
        current_feature = new_feature()
        current_feature["properties"]["name"] = r[7]
        current_feature["properties"]["state"] = r[8]
        current_feature["id"] = str(const_count)
        const_count = const_count + 1


    # Aggregate the coordinates
    current_feature["geometry"]["points"].append([float(r[0]), float(r[1])])

print "Total constituencies: ", len(geojson["features"])

# Reduce the polygons



# output
fout = open(rootpath + "/../web/static/constituencies.json","w")
fout.write(json.dumps(geojson,indent=4, separators=(',', ': ')))
# fout.write(json.dumps(geojson))
fout.close()


