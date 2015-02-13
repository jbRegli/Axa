import sys
import os
import time

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


def test():
    dirs = [f for f in os.listdir('./Data/drivers/')]

    l_dirs = len(dirs)

    tic = time.clock()
    k = 1

    driver = 1892
    trip = 121
    data = ED.extractTrip(driver, trip)

    feature_dic = length.Length(data, {})
    feature_dic = speed.Speed(data, feature_dic)
    feature_redic = acc.Acceleration(data, feature_dic)
    feature_dic = length.Length(data, feature_dic)
    feature_dic = ts.TurningSpeed(data, feature_dic)

    path = "./Data/Features/" + str(driver)
    name = str(trip) + ".csv"

    feature_dic['driver'] = driver

    SF.storeFeature(feature_dic, path, name, 0)


    tac = time.clock() - tic

    print tac

    return feature_dic



