import sys
import os
import time

from joblib import Parallel, delayed
import multiprocessing
"""
# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(10)
def processInput(i):
    return i * i

num_cores = multiprocessing.cpu_count()

results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
"""
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


def generateFeature_all():
    dirs = [f for f in os.listdir('./Data/drivers/')]

    l_dirs = len(dirs)
    tic = time.clock()
    k = 1
    discard_trip = []

    num_cores = multiprocessing.cpu_count()

    for driver in dirs:
        print("Driver %i on %i (driver %s)") %(k, l_dirs, driver)
        files = [f[0:-4] for f in os.listdir('./Data/drivers/'+str(driver))]

        #discard_trip_temp = process_trip(driver)

        discard_trip_temp =Parallel(n_jobs=num_cores)\
                                  (delayed(process_trip)(trip,driver) for trip in files)

        for elt in discard_trip_temp:
            discard_trip.append(elt)

        k+=1

    tac = time.clock() - tic

    print(" ")
    print("There has been %i discarded trips") %len(discard_trip)
    print(" ")
    print("Tac= ", str(tac))

    print(" ")
    print("Merging into one csv")
    data = CB.combineSupervize("./Data/Features","test.csv", "./Data/Features/")

    return tac, discard_trip






def process_trip(trip, driver):
    #files = [f[0:-4] for f in os.listdir('./Data/drivers/'+str(driver))]

    #l = 1
    #for trip in files:
        #l_trip = str(len(files))

        #sys.stdout.write("\r\x1b[K" + "     Trip " + str(l) + "/"  \
                                    #+ l_trip + " -- trip " + trip)
        #sys.stdout.flush()

        #driver = 1
        #trip = 1
    data = ED.extractTrip(driver, trip)
    discard_trip = []
    feature_dic = length.Length(data, {})

    if feature_dic == 0:
        discard_trip.append({driver,trip})
        return discard_trip

    feature_dic = speed.Speed(data, feature_dic)
    if feature_dic == 0:
        discard_trip.append({driver,trip})
        return discard_trip

    feature_dic = acc.Acceleration(data, feature_dic)
    if feature_dic == 0:
        discard_trip.append({driver,trip})
        return discard_trip

    feature_dic = length.Length(data, feature_dic)
    if feature_dic == 0:
        discard_trip.append({driver,trip})
        return discard_trip

    feature_dic = ts.TurningSpeed(data, feature_dic)
    if feature_dic == 0:
        discard_trip.append({driver,trip})
        return discard_trip

    path = "./Data/Features/" + str(driver)
    name = str(trip) + ".csv"

    feature_dic['driver'] = int(driver)

    SF.storeFeature(feature_dic, path, name, 0)
        #l+=1




