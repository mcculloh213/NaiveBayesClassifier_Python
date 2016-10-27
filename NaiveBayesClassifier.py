import sys
import lib.load
import lib.logger as lg
import lib.split

__author__ = "H.D. 'Chip' McCullough IV"


if __name__ == '__main__':
    log = lg.Logger("NBC", "main", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    try:
        log.logger.info("Loading data set from {0}".format(sys.argv[1]))
        dataset = lib.load.loadCSV(sys.argv[1])            # Load input from command line into NBC
        log.logger.info("Splitting data set using default parameters")
        train, test = lib.split.splitDataSet(dataset)      # Split data set
    except Exception as e:
        log.logger.exception(e)
