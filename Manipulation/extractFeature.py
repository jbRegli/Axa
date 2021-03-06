"""
Function  an extracted feature in a given .csv file
"""
import csv
import os
import numpy as np

def extractFeature(feature, load_dir, load_name):
    r"""
    Store the extracted feature in a fileName.csv

    -------
    INPUTS:
    -------
    feature: dic : feature{name} = feature.value
    """
    # Extract csv in dictionary
    with open(os.path.join(load_dir, load_name), 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            feature = row

    # Convert dic.values() to np.Array
    for key in feature:
        feature[key] = np.array(feature[key])

    return feature
