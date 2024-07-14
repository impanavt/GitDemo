# to use looging mesaages accross all tests instead of creting seperately can use in test cases using inheritance concept

import logging
import inspect


class BaseClass:
  def getLogger(self):
    # gives name from which method is called
    loggerName=inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.DEBUG)
    return logger