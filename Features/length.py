"""
Extract the length of the trip
"""
import numpy as np

def Length(data, feature_dic):
    r"""
    Compute the length overall trip
    """
    # Convert the data:
    np_x = np.array(data.x)
    np_y = np.array(data.y)

    # Update the feature dictionary
    feature_dic['length'] = np.size(np_x)

    return feature_dic

