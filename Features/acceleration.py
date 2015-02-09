"""
Extract the speed of the drivers
"""
import numpy as np

def Acceleration(data, feature_dic):
    r"""
    Compute the acceletation along x, y and overall
    """
    # Get the requiered data:
    v_x = feature_dic['v_x']
    v_y = feature_dic['v_y']
    v = feature_dic['v']

    # Shifted by 1 data:
    v_x1 = np.roll(v_x, 1)
    v_y1 = np.roll(v_y, 1)
    v1 = np.roll(v, 1)

    # Accelerations:
    a_x = (np.absolute(v_x) - np.absolute(v_x1)) / 3.6
    a_y = (np.absolute(v_y) - np.absolute(v_y1)) / 3.6
    a = (np.absolute(v) - np.absolute(v1)) / 3.6

    a_x[0] = 0
    a_y[0] = 0
    a[0] = 0
    a_x[1] = 0
    a_y[1] = 0
    a[1] = 0

    # Create the feature dictionary
    feature_dic['a_x'] = a_x
    feature_dic['a_y'] = a_y
    feature_dic['a'] = a

    feature_dic['a_mean'] = np.mean(a)
    feature_dic['a_x_mean'] = np.mean(a_x)
    feature_dic['a_y_mean'] = np.mean(a_y)

    feature_dic['a_std'] = np.std(a)
    feature_dic['a_x_std'] = np.std(a_x)
    feature_dic['a_y_std'] = np.std(a_y)

    # Acceleration:
    acc_x = a_x[a_x>0]
    acc_y = a_y[a_y>0]
    acc = a[a>0]

    feature_dic['acc_x'] = acc_x
    feature_dic['acc_y'] = acc_y
    feature_dic['acc'] = acc

    feature_dic['acc_x_max'] = max(acc_x)
    feature_dic['acc_y_max'] = max(acc_y)
    feature_dic['acc_max'] = max(acc)

    feature_dic['acc_x_mean'] = np.mean(acc_x)
    feature_dic['acc_y_mean'] = np.mean(acc_y)
    feature_dic['acc_mean'] = np.mean(acc)

    feature_dic['acc_x_std'] = np.std(acc_x)
    feature_dic['acc_y_std'] = np.std(acc_y)
    feature_dic['acc_std'] = np.std(acc)

    feature_dic['acc_x_len'] = acc_x.size
    feature_dic['acc_y_len'] = acc_y.size
    feature_dic['acc_len'] = acc.size

    # Braking:
    limit = -0.05
    br_x = a_x[a_x < limit]
    br_y = a_y[a_y < limit]
    br = a[a < limit]

    feature_dic['br_x'] = br_x
    feature_dic['br_y'] = br_y
    feature_dic['br'] = br

    feature_dic['br_x_min'] = min(br_x)
    feature_dic['br_y_min'] = min(br_y)
    feature_dic['br_min'] = min(br)

    feature_dic['br_x_mean'] = np.mean(br_x)
    feature_dic['br_y_mean'] = np.mean(br_x)
    feature_dic['br_mean'] = np.mean(br)

    feature_dic['br_x_std'] = np.std(br_x)
    feature_dic['br_y_std'] = np.std(br_x)
    feature_dic['br_std'] = np.std(br)

    feature_dic['br_x_len'] = br_x.size
    feature_dic['br_y_len'] = br_x.size
    feature_dic['br_len'] = br.size

    # Acceleration iddle
    a_x_iddle = a_x[a_x<=0][a_x[a_x<=0] >limit]
    a_y_iddle = a_y[a_y<=0][a_y[a_y<=0] >limit]
    a_iddle = a[a<=0][a[a<=0] >limit]

    feature_dic['a_x_iddle'] = a_x_iddle
    feature_dic['a_x_iddle_len'] = a_x_iddle.size

    feature_dic['a_y_iddle'] = a_y_iddle
    feature_dic['a_y_iddle_len'] = a_y_iddle.size

    feature_dic['a_iddle'] = a_iddle
    feature_dic['a_iddle_len'] = a_iddle.size

    return feature_dic

