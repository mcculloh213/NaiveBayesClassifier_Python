import random
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.split", "splitDataSet", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def splitDataSet(data, split=0.67):
    """
    Split the passed data based on param:split to build and test assumptions.
    :param data: Data set from parsed CSV file
    :type data: <list(float[])>
    :param split: Percentage of data to use to train NBC, default is 67% (2/3), leaving 33% to test the model.
    :type split: double
    :return: [train, test]
    """
    trainSize = int(len(data) * split)                     # Get the size of the training data using param:split
    log.logger.info("Training data size set to {0}".format(trainSize))
    log.logger.info("Initializing training data set")
    train = []                                             # Initialize an empty array to hold training data
    test = list(data)                                      # Copy the passed data
    log.logger.info("Building training and testing data sets")
    while len(train) < trainSize:                          # Build the training set
        index = random.randrange(len(test))                # Get a random row from the data
        train.append(test.pop(index))                      # Remove it from the data, and append it to the training data
    log.logger.info("Done -- Returning split data set")
    return [train, test]                                   # Return the split data set
