import lib.logger as lg
import lib.probability
__author__ = "H.D. 'Chip' McCullough IV"


def predict(summary, inputVec):
    """
    Predict label of param:inputVec based on param:summary
    :param summary: Summary (mean, variance, st.dev) dictionary
    :type summary: dict
    :param inputVec: input row of data
    :type inputVec: array
    :return: Label Prediction (str)
    """
    probabilities = lib.probability.classProbabilities(summary, inputVec)
    labelPrediction, probabilityPrediction = None, -1
    for classValue, probability in probabilities.items():
        if labelPrediction is None or probability > probabilityPrediction:
            probabilityPrediction = probability
            labelPrediction = classValue
    return labelPrediction


def getPredictions(summary, testSet):
    """
    Run label predictions on param:testSet.
    :param summary: Summary (mean, variance, st.dev) dictionary
    :type summary: dict
    :param testSet: Data test set
    :return: Predictions (str[])
    """
    predictions = []
    for i in range(len(testSet)):
        result = predict(summary, testSet[i])
        predictions.append(result)
    return predictions
