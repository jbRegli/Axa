"""
Extract the speed of the drivers
"""
import numpy as np

def Speed(data, feature_dic):
    r"""
    Compute the speed along x, y and overall
    """
    # Convert the data:
    np_x = np.array(data.x)
    np_y = np.array(data.y)

    # Shifted by 1 data:
    np_x1 = np.roll(np_x, 1)
    np_y1 = np.roll(np_y, 1)

    # Speeds:
    v_x = (np_x - np_x1) * 3.6
    v_y = (np_y - np_y1) * 3.6

    v = np.sqrt(np.power(np_x - np_x1,2) + np.power(np_y - np_y1,2)) \
            * 3.6

    v_x[0] = 0
    v_y[0] = 0
    v[0] = 0

    # Create the feature dictionary
    feature_dic['v_x'] = v_x
    feature_dic['v_y'] = v_y
    feature_dic['v'] = v

    feature_dic['v_mean'] = np.mean(v)
    feature_dic['v_x_mean'] = np.mean(v_x)
    feature_dic['v_y_mean'] = np.mean(v_y)

    feature_dic['v_std'] = np.std(v)
    feature_dic['v_x_std'] = np.std(v_x)
    feature_dic['v_y_std'] = np.std(v_y)

    feature_dic['v_max'] = max(v)

    # Iddle time
    v_x_iddle = v_x[v_x==0]
    v_y_iddle = v_y[v_y==0]
    v_iddle = v[v==0]

    feature_dic['v_x_iddle'] = v_x_iddle
    feature_dic['v_x_iddle_len'] = v_x_iddle.size

    feature_dic['v_y_iddle'] = v_y_iddle
    feature_dic['v_y_iddle_len'] = v_y_iddle.size

    feature_dic['v_iddle'] = v_iddle
    feature_dic['v_iddle_len'] = v_iddle.size


    return feature_dic


