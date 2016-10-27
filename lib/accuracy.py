import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.accuracy", "accuracy", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def accuracy(testSet, predictions):
    """
    Determine model accuracy based on test data set class variables and correlating predicted class variables
    :param testSet: Test set used to estimate predictions
    :param predictions: Class predictions
    :return: Accuracy (float)
    """
    log.logger.info("Accuracy: Running accuracy checks against test set")
    num_correct = 0
    for x in range(0, len(testSet)):
        if testSet[x][-1] == predictions[x]:
            num_correct += 1
            log.logger.info("Accuracy: Number correct increased to {0}".format(num_correct))
    acc = (num_correct/float(len(testSet))) * 100.0
    log.logger.info("Accuracy: Done -- Returning accuracy of model")
    return acc
