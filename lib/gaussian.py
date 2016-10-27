import math
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.gaussian", "gaussian", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def gaussian(x, mu, sigma):
    """
    Estimate probability of param:x based on Normal (Gaussian) distribution.
    :param x: Random Variable
    :param mu: Expected Value
    :param sigma: Standard Deviation
    :return: Probability (float)
    """
    log.logger.info("Gaussian: Estimating probability")
    exp = math.exp(-(math.pow(x - mu, 2) / (2 * math.pow(sigma, 2))))
    probability = (1 / (math.sqrt(2*math.pi) * sigma)) * exp
    log.logger.info("Gaussian: Done -- Returning estimated probability")
    return probability
