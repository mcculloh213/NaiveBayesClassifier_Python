import sys
import lib.load
import lib.logger as lg
import lib.split
import lib.summary
import lib.predict

__author__ = "H.D. 'Chip' McCullough IV"


if __name__ == '__main__':
    log = lg.Logger("NBC", "main", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    try:
        log.logger.info("Loading data set from {0}".format('./data/prima-indians-diabetes.csv'))
        dataset = lib.load.loadCSV('./data/prima-indians-diabetes.csv')            # Load input from command line into NBC
        log.logger.info("Splitting data set using default parameters")
        train, test = lib.split.splitDataSet(dataset)                # Split data set
        log.logger.info("Summarizing training data")
        summaries = lib.summary.classSummary(train)                  # Summarize training data
        log.logger.info("Predict probabilities of testing data")
        predictions = lib.predict.getPredictions(summaries, test)    # Estimate probabilities based on traning set stats
        log.logger.info("Debug line")
    except Exception as e:
        log.logger.exception(e)
