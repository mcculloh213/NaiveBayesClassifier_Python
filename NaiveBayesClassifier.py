import sys
import lib.accuracy
import lib.load
import lib.logger as lg
import lib.split
import lib.summary
import lib.predict
import lib.write

__author__ = "H.D. 'Chip' McCullough IV"


if __name__ == '__main__':
    log = lg.Logger("NBC", "main", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    try:
        log.logger.info("Loading data set from {0}".format(sys.argv[1]))
        dataset = lib.load.loadCSV(sys.argv[1])                           # Load input from command line into NBC
        log.logger.info("Splitting data set using default parameters")
        train, test = lib.split.splitDataSet(dataset)                     # Split data set
        log.logger.info("Summarizing training data")
        summaries = lib.summary.classSummary(train)                       # Summarize training data
        log.logger.info("Predict probabilities of testing data")
        predictions = lib.predict.getPredictions(summaries, test)         # Estimate probabilities based on training set
        log.logger.info("Estimating accuracy of predictions")
        accuracy = lib.accuracy.accuracy(test, predictions)               # Calculate accuracy of model
        log.logger.info("The model displayed {0}% accuracy when predicting class variables.".format(accuracy))
        if len(sys.argv) == 3:
            log.logger.info("Loading data set from {0}".format(sys.argv[2]))
            missingClass = lib.load.loadCSV(sys.argv[2])                  # Load data to run predictions on
            log.logger.info("Predicting probabilities of data")
            prob = lib.predict.getPredictions(summaries, missingClass)    # Estimate probabilities based on training set
            lib.write.writeData(missingClass, prob, sys.argv[1], accuracy)
    except Exception as e:
        log.logger.exception(e)
