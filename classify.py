import sys
import os
import time

import pandas as pd

import addPath
sys.path = addPath.addPath(sys.path)

import storeFeature as SF
import extractFeature as EF
import extractData as ED
import speed
import acceleration as acc
import turningSpeed as ts
import length
import combineSupervize as CB

def classify():
    # Extract as a pandas dataframe:
    dataset = ED.extractSupervise(file_name="data.csv",
                                  data_path="./Data/Features/")
    # Convert to dictionary:
    # dataset.to_dict()

    # Remove useless column:
    # dataset.pop('Unnamed: 0')

    #Shuffle the dataset:
    train = pd.DataFrame()
    test = pd.DataFrame()

    for driver in pd.unique(dataset.driver):
        temp = dataset.loc[dataset['driver'] == 1768]

    dataY = dataset.driver
    dataX =  dataset.drop('driver', 1)
    return dataset
