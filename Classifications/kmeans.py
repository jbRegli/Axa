import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
"""
K Neighbors classifier
Meta-parameters:
    n_neighbors : int
    number of neighbors used for the classification
"""

def train_classifier(xTrain_s, yTrain_s, kwargs):
    """
    Train a naive baise classifier on xTrain and yTrain and return the trained
    classifier
    """
    if type(xTrain_s) != list:
        classifier_s = KNeighborsClassifier(**kwargs)
        classifier_s.fit(xTrain_s, yTrain_s)

    else:
        classifier_s = train_classifier_8(xTrain_s, yTrain_s, kwargs)

    return classifier_s


def predict_proba(classifier_s, dataset_s):
    """
    Given a dataset and a classifier, compute the proba prediction
    This function can be use for validation as well as for the test.
    """
    if type(classifier_s) != list:
        # Probability of being in each label
        proba_predicted_s = classifier_s.predict_proba(dataset_s) #[:,1]

    else:
        proba_predicted_s = predict_proba_8(classifier_s, dataset_s)

    return proba_predicted_s


def get_classification_error(y_predicted_s, y_true_s, normalize= True):

    prediction_error_s = accuracy_score(y_true_s, y_predicted_s,
                                            normalize=normalize)

    return prediction_error_s
