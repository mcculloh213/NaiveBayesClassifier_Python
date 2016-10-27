import os
import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("NBC.write", "writeData", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def writeData(data, predictions, f_in, accuracy):
    title = os.path.split(f_in)[-1].split('.')[0]
    filepath = os.path.join(".", "data", title + "-predictions.csv")
    fpabout = os.path.join(".", "data", title + "-predictions-about.txt")
    log.logger.info("writeData: Creating outfile: {0}".format(filepath))
    with open(fpabout, 'w') as w:
        w.write("This data was generated using a model that was {0}% "
                "accurate on the test subset of the original data, \"{1}\"\n".format(accuracy, f_in))
    with open(filepath, 'w') as w:
        for i in range(0, len(data)):
            toFile = ""
            for j in range(0, len(data[i])):
                toFile += (str(data[i][j]) + ",")
            toFile += str(int(predictions[i]))
            w.write(toFile + "\n")
    log.logger.info("writeData: Done -- EOP")
