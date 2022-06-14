# imports
from genericpath import isdir
import logging
import os
from datetime import date

class Logger:
    currentDate = date.today().strftime("%d-%m-%Y")

    #Create Logs Directory and Today's Folder
    directoryPath = os.path.dirname(os.path.abspath(__file__))
    logPath = directoryPath+'\Logs'
    try:
        if (os.path.isdir(logPath)):
            pass
        else:
            os.mkdir(logPath)
            logging.info('Directory for Logs created')
    except OSError as error:
        logging.error("OSError",exc_info=True)
    
    logging.basicConfig(level='INFO',filemode='a',filename='Logs/'+currentDate+'.txt',format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

    def getLogger(name):
        logger = logging.getLogger(name)
        return logger

    def infoLog(self, message):
        logging.info(message)
    
    def debugLog(self, message):
        logging.debug(message)

    def warningLog(self, message):
        logging.warning(message)
    
    def errorLog(self, message):
        logging.error(message,exc_info=True)

    def criticalLog(self, message):
        logging.critical(message,exc_info=True)

if __name__ == "__main__":

    logger = Logger()

    logger.infoLog("This is Info")
    logger.debugLog("This is Debug")
    logger.warningLog("This is Warning")
    logger.errorLog("This is Error")
    logger.criticalLog("This is Critical")