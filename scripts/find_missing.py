__author__ = 'dhanannjay.deo'

"""
This works on top of the geojson file created by csv_to_json script
It compares the constituencies with the parliament.csv to find out missing constituencies

"""
import json
import csv
import sys
import os
rootpath = os.path.abspath(os.path.dirname(__file__))
from Polygon.Utils import reducePoints

decimation_factor = 0.2
reader = csv.reader(open(rootpath + "/../data/parliament.csv"), skipinitialspace=True)

fin = open(rootpath + "/../web/static/constituencies.json","r")
geojson = json.loads(fin.read())

constituency_list = [afeature["properties"]["name"].upper() for afeature in geojson["features"]]
# print constituency_list

constituency_in_data = []

found = []
missing = []

current = ""
count = 0
for r in reader:
    if r[0] == '2009':
        if current != r[2]:
            # New constituency
            current = r[2]
            constituency_in_data.append(current)
            count = count + 1
            if current in constituency_list:
                print count, ", Got: ", r[2]
                found.append(r[2])
            else:
                print count, "#######, Missing : ", r[2]
                missing.append(r[2])

# Now find out what remains of constituency_list
for afeature in found:
    constituency_list.remove(afeature)


print "Constituency list"
print "#################"
print sorted(constituency_list)
print "Missing"
print "#######"
print sorted(missing)



# Reduce the polygons


#
# # output
# fout.write(json.dumps(geojson,indent=4, separators=(',', ': ')))
# # fout.write(json.dumps(geojson))
# fout.close()


