import lib.gaussian
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.probability", "classProbability", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def classProbabilities(summary, inputVec):
    """
    Estimate class probabilities using lib.gaussian.gaussian()
    :param summary: Summary (mean, variance, st.dev) dictionary
    :type summary: dict
    :param inputVec: input row of data
    :type inputVec: array
    :return: Probabilities dict{"class": float[]}
    """
    log.logger.info("classProbabilities: Initializing probability dictionary")
    probabilities = {}
    log.logger.info("classProbabilities: Estimating probabilities")
    for classValue, classSummary in summary.items():
        probabilities[classValue] = 1
        for i in range(0, len(classSummary)):
            mean, var, stdev = classSummary[i]
            x = inputVec[i]
            probabilities[classValue] *= lib.gaussian.gaussian(x, mean, stdev)
    log.logger.info("classProbabilities: Done -- Returning probabilities by class")
    return probabilities
