"""
This is a mongo repository module
"""
import mongoengine
from mongoengine import ConnectionFailure
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

from app.settings.settings import Settings
from loguru import logger


class MongoDB:
    def __init__(self):
        self.__set_connection()

    def __set_connection(self):
        try:
            logger.debug('Connecting to Mongo')
            self.client = mongoengine.connect(host=Settings().MONGODB_URI)
            logger.debug('Connected to Mongo')
        except ConnectionFailure as err:
            if "Use disconnect() first" in err.args[0]:
                self.client = mongoengine.get_connection()

    def check_connection(self):
        try:
            self.client.server_info()
            return True
        except ServerSelectionTimeoutError as err:
            logger.critical(f"{err}")
            return False
        except OperationFailure as err:
            logger.critical(f"{err}")
            return False
