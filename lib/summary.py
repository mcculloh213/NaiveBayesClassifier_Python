import lib.logger as lg
import lib.separate
import lib.statistics

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.summary", "summary", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def summary(data):
    """
    Summarize param:data
    :param data: Data set
    :type data: list<float[]>
    :return: Summary (float[])
    """
    log.logger.info("Summarizing data")
    summ = []
    for attribute in zip(*data):
        summ.append((lib.statistics.mean(attribute),       # Find attribute E[X]
                     lib.statistics.var(attribute),        # Find attribute V[X}
                     lib.statistics.stdev(attribute)))     # Find attribute St.Dev[X]
    log.logger.info("Removing summary related to class variable")
    del summ[-1]                                           # Delete class variable summary
    log.logger.info("Done -- Returning summarized data")
    return summ


def classSummary(data):
    """
    Summarize param:data by class variables
    :param data: Data set
    :type data: list<float[]>
    :return:
    """
    log.logger.info("Separating data by class value")
    separated = lib.separate.separateClasses(data)         # Separate data
    summaries = {}
    log.logger.info("Summarize data by class value")
    for classValue, instances in separated.iteritems():    # Iterate through separated data
        summaries[classValue] = summary(instances)         # Summarize
    log.logger.info("Done -- Returning summarized data")
    return summaries
