__author__ = 'dhanannjay.deo'

"""
Goal is to interprete the csv files for constituency map, and the election results,
and write back in geo-json format which will be easy to read by webapp

{"type":"Feature","id":"01","properties":{"name":"Alabama","density":94.65},"geometry":{"type":"Polygon","coordinates":[[[-87.359296,35.00118], .. ]]}},

"""

import csv
import sys
import os
rootpath = os.path.abspath(os.path.dirname(__file__))

reader = csv.reader(open(rootpath + "/../data/india_spatial.csv"), skipinitialspace=True)

count = -1
geojson = {"type":"FeatureCollection",
           "features": []}


current_feature = {"name": ""}

for r in reader:
    # Skip first row of titles
    count = count + 1
    if count == 0:
        print "Skip"
        continue

    # Find out if we are dealing with the same constituency
    if r[7] != current_feature["name"]:
        # Not so create a new feature and insert current feature
        geojson["features"].append(current_feature)
        current_feature = {"name": r[7]}
        print "New constituency: ", r[7]

print "Total constituencies: ", len(geojson["features"])

