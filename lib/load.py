import csv
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.load", "loadCSV", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def loadCSV(file):
    """
    Load CSV file into a list to be passed off.
    :param file: Absolute path to file.
    :type file: str
    :return: dataset<list(float[])>
    """
    try:
        log.logger.info("Opening {0}".format(file))
        f = open(file, 'r')                                # Open param:file
        log.logger.info("Reading file")
        data = csv.reader(f)                               # Read the file using csv.reader
        log.logger.info("Cohersing data into a list")
        dataset = list(data)                               # Convert csv data into a list
        log.logger.info("Converting data entries from strings to floats")
        for i in range(0, len(dataset)):                   # Cast data into floats
            dataset[i] = [float(x) for x in dataset[i]]
        log.logger.info("Done -- Closing input file")
        f.close()                                          # Close param:file
        return dataset
    except Exception as e:
        log.logger.exception(e)                            # Log exception
