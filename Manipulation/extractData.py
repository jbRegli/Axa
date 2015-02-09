"""
Function extracting the data from a trip of a driver
"""
#!/usr/bin/env python
#
# [SNIPPET_NAME: CSV to Dictionary]
# [SNIPPET_CATEGORIES: csv]
# [SNIPPET_DESCRIPTION: Read a CSV file to a dictionary of dictionaries]
# [SNIPPET_AUTHOR: Bruno Girin <brunogirin@gmail.com>]
# [SNIPPET_LICENSE: GPL]

# This snippet demonstrates how to read a CSV file into a dictionary of
# dictionaries in order to be able to query it easily.
# The full documentation for the csv module is available here:
# http://docs.python.org/library/csv.html
#
# The data used in the companion csv2dict.csv file was taken from here:
# http://www.trainweb.org/tubeprune/Statistics.htm
# See, you can even learn some interesting facts about the London Underground
# network while learning Python.

#
# First things first, we need to import the csv module
# Also import sys to get argv[0], which holds the name of the script
#
import os
import pandas as pd

#################################

def extractTrip(driver_n, trip_n, data_path="./Data/drivers/"):
    # Data path:
    data_path = data_path + str(driver_n) + "/"
    # Extract the data:
    file_name = str(trip_n) + ".csv"

    csvFile = os.path.join(data_path, file_name)

    colnames = ['x', 'y']
    data = pd.read_csv(csvFile, skiprows=[0], names=colnames)

    return data
