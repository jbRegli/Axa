import sys
import os

import addPath
sys.path = addPath.addPath(sys.path)

import storeFeature as SF
import extractFeature as EF
import extractData as ED
import speed
import acceleration as acc
import turningSpeed as ts
import length

def test():
    dirs = [f for f in os.listdir('./Data/drivers/')]

    #for driver in dirs:
    #    files = [f[0:-4] for f in os.listdir('./Data/drivers/'+str(driver))]
    #    for trip in files:
    driver = 1
    trip = 1
    data = ED.extractTrip(driver, trip)

    feature_dic = speed.Speed(data, {})
    feature_dic = acc.Acceleration(data, feature_dic)
    feature_dic = length.Length(data, feature_dic)
    feature_dic = ts.TurningSpeed(data, feature_dic)

    path = "./Data/Features/" + str(driver)
    name = str(trip) + ".csv"

    SF.storeFeature(feature_dic, path, name)

    return feature_dic



