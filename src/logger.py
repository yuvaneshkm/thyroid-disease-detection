# Importing necessary libraries:
import os
import logging
from datetime import datetime


FILE_NAME = f"{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log"

LOG_FILE_DIRECTORY = os.path.join(os.getcwd(), 'logs')
os.makedirs(LOG_FILE_DIRECTORY, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FILE_DIRECTORY, FILE_NAME)

# configure logging:
logging.basicConfig(
    filename = LOG_FILE_PATH,
    level = logging.INFO,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)


if __name__=="__main__":
    from src.exception import CustomException
    logging.info("Logging Started")
    try:
        89/0
    except Exception as ex:
        logging.info(CustomException(ex))
    logging.info('Logging Compleetd')