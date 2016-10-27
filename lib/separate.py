import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.separate", "separateClasses", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def separateClasses(data):
    """
    Separate param:data by class variable, which is the last variable in the array of floats.
    :param data: data to be separated by class variable
    :return: dict{"classVar0": data, ..., "classVarN: data}
    """
    log.logger.info("Initializing empty dictionary")
    classMap = {}                                          # Initialize empty dictionary
    log.logger.info("Iterating through the data")
    for i in range(0, len(data)):                          # Iterate through data
        vec = data[i]                                      # Pull a line from the data
        if vec[-1] not in classMap:                        # Check if class variable has been mapped
            log.logger.info("Adding class variable {0} to the dictionary".format(vec[-1]))
            classMap[vec[-1]] = []                         # If it hasn't, add it to the map
        classMap[vec[-1]].append(vec)                      # Add the line to the appropriate mapping
    log.logger.info("Done -- Returning data separated by class variables")
    return classMap
