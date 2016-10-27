import lib.logger as lg
import lib.separate
import lib.statistics

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.summary", "summary", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def summary(data, rm):
    """
    Summarize param:data
    :param data: Data set
    :type data: list
    :param rm: Remove last row
    :type rm: bool
    :return: Summary (float[])
    """
    log.logger.info("Summary: Summarizing data")
    summ = []
    for attribute in zip(*data):
        summ.append((lib.statistics.mean(attribute),       # Find attribute E[X]
                     lib.statistics.var(attribute),        # Find attribute V[X]
                     lib.statistics.stdev(attribute)))     # Find attribute St.Dev[X]
    log.logger.info("Summary: Removing summary related to class variable")
    if rm:
        del summ[-1]                                           # Delete class variable summary
    log.logger.info("Summary: Done -- Returning summarized data")
    return summ


def classSummary(data, rm=True):
    """
    Summarize param:data by class variables
    :param data: Data set
    :type data: list
    :param rm: Remove last row
    :type rm: bool
    :return:
    """
    log.logger.info("classSummary: Separating data by class value")
    separated = lib.separate.separateClasses(data)         # Separate data
    summaries = {}
    log.logger.info("classSummary: Summarize data by class value")
    for classValue, instances in separated.items():        # Iterate through separated data
        summaries[classValue] = summary(instances, rm)     # Summarize
    log.logger.info("classSummary: Done -- Returning summarized data")
    return summaries
