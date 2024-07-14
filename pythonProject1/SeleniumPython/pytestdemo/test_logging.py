import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    # parent file handling of file location
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
     fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler object
    # finally logger object will have knowledge of fiel handling

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")
