__author__ = 'dhanannjay.deo'

"""
Goal is to interprete the csv files for constituency map, and the election results,
and write back in json which will be easy to read by webapp
"""

import csv

reader = csv.reader(['1997,Ford,E350,"Sample,  csv field with embedded comma and quote"'], skipinitialspace=True)
for r in reader:
    print r