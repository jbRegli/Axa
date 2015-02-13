"""
Function saving an extracted feature in a given .csv file
"""
import csv
import os
import extractFeature as EF

def storeFeature(feature, save_dir, save_name, verb=1):
    r"""
    Store the extracted feature in a fileName.csv

    -------
    INPUTS:
    -------
    feature: dic : feature{name} = feature.value
    """
    # Creating the folder if necessary
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    else:
        # List all the file in this folder
        files = [f[0:-4] for f in os.listdir(save_dir)]

        if save_name in files:
            # If this csv already exist -> update it
            feature_old = EF.extractFeature(feature, save_dir, save_name)

            for key in feature_old:
                if key not in feature:
                    print("adding...")
                    feature[key] = feature_old[key]

    # Saving the feature:
    saveFeature(feature, save_dir, save_name, verb)


def saveFeature(feature, save_dir, save_name, verb=1):
    # Saving the feature:
    with open(os.path.join(save_dir, save_name), 'w') as outfile:
        csvWriter = csv.DictWriter(outfile, fieldnames=feature.keys())

        csvWriter.writeheader()
        csvWriter.writerow(feature)

        if verb == 1:
            print("File saved in ", os.path.join(save_dir, save_name))

