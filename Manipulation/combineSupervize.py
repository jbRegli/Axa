"""
Function extracting the saved features and aving it in a .csv file
"""
import csv
import os
import pandas as pd

import extractFeature as EF

def combineSupervize(save_dir, save_name, load_dir="./Data/Features/", verb=1):
    r"""
    Store the extracted feature in a fileName.csv

    -------
    INPUTS:
    -------
    feature: dic : feature{name} = feature.value
    """
    dirs = [f for f in os.listdir(load_dir)]

    data_f = pd.DataFrame()
    list_features = []

    first = True

    for driver in dirs:
        files = [f[0:-4] for f in os.listdir(load_dir + str(driver))]
        print str(driver)

        for trip in files:
            csvFile = load_dir + str(driver) + "/" + str(trip) + ".csv"

            features = pd.read_csv(csvFile, header=0)

            # Delete useless columns
            del features['v_x']
            del features['v_y']
            del features['v']
            del features['v_x_iddle']
            del features['v_y_iddle']
            del features['v_iddle']


            del features['radius']
            del features['rad/v']
            del features['direction']

            del features['a']
            del features['a_x']
            del features['a_y']
            del features['a_x_iddle']
            del features['a_y_iddle']
            del features['a_iddle']

            del features['acc']
            del features['acc_x']
            del features['acc_y']

            del features['br']
            del features['br_x']
            del features['br_y']

            if first == True:


                features.to_csv(os.path.join(save_dir, save_name))
                first = False
            else:
                 features.to_csv(os.path.join(save_dir, save_name),
                                    mode='a',
                                    header=False)


    return 0
