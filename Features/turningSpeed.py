"""
Extract the speed of the drivers
"""
import numpy as np

def TurningSpeed(data, feature_dic):
    r"""
    Compute the acceletation along x, y and overall
    """
    # Convert the data:
    np_x = np.array(data.x)
    np_y = np.array(data.y)

    # Shifted by 1 data:
    np_x1 = np.roll(np_x, 1)
    np_y1 = np.roll(np_y, 1)

    np_x1[0] = 0
    np_y1[0] = 0

    # Distance:
    d = np.sqrt(np.power(np_x - np_x1,2) + np.power(np_y - np_y1,2))

    # Direction:
    theta = np.arctan(np.absolute(np_y - np_y1)/np.absolute(np_x - np_x1))

    theta[np.isnan(theta)]=0
    theta_1 = np.roll(theta,1)

    # Radius:
    radius = d * np.tan(np.pi/2 - (theta - theta_1))

    radius[np.isnan(radius)] = 0
    radius[radius > 300] = 0
    radius[radius < -300] = 0

    # Radius over speed:
    rad_v = np.absolute(radius / feature_dic['v'])
    rad_v[np.isnan(rad_v)]=0


    # Update the feature dictionary
    feature_dic['direction'] = theta

    feature_dic['radius'] = radius

    feature_dic['rad/v'] = rad_v
    feature_dic['rad/v_mean'] = np.mean(rad_v)
    feature_dic['rad/v_std'] = np.std(rad_v)

    return feature_dic

