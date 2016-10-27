import math
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.statistics", "stats", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def mean(nums):
    """
    Calculate Expected Value of param:nums
    :param nums: Numbers to find Expected Value of
    :type nums: float[]
    :return: Expected Value (float)
    """
    log.logger.info("Calculating Expected Value")
    numerator = sum(nums)                                  # Sum the entries of param:nums
    denominator = float(len(nums))                         # Count the number of entries in param:nums
    log.logger.info("Done -- Returning Expected Value")
    return numerator/denominator


def var(nums):
    """
    Calculate Variance of param:nums using N-1 formula
    :param nums: Numbers to find Variance of
    :type nums: float[]
    :return: Variance (float)
    """
    log.logger.info("Calculating Variance")
    mu = mean(nums)                                  # Calculate the EV
    variance = sum([pow(x - mu, 2) for x in nums]) / float(len(nums) - 1)
    log.logger.info("Done -- Returning Variance")
    return variance


def stdev(nums):
    """
    Calculate the Standard Deviation of param:nums using N-1 Variance formula
    :param nums: Numbers to find St. Dev of
    :type nums: float[]
    :return: St. Dev (float)
    """
    log.logger.info("Calculating St. Dev")
    sigma = math.sqrt(var(nums))
    log.logger.info("Done -- Returning St. Dev")
    return sigma
