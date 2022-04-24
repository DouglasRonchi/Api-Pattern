"""
This is a mongo repository module
"""
import mongoengine
from mongoengine import ConnectionFailure
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

from app.settings.settings import Settings
from loguru import logger

from app.utils.singleton import Singleton


class MongoDB(metaclass=Singleton):
    def connect(self, db: str = None, host: str = None):
        """
        :param db: The database name to connect
        :param host: The Host name to connect to Mongo
        :return: None
        """
        try:
            logger.debug("Getting settings to connect to Mongo")
            host = Settings().MONGODB_URI if not host else host
            logger.debug('Connecting to Mongo')
            self.client = mongoengine.connect(db=db, host=host)
            logger.debug('Connected to Mongo')
        except ConnectionFailure as err:
            if "Use disconnect() first" in err.args[0]:
                self.client = mongoengine.get_connection()

    def check_connection(self):
        try:
            if not self.client:
                return False
            self.client.server_info()
            return True
        except ServerSelectionTimeoutError as err:
            logger.critical(f"{err}")
            return False
        except OperationFailure as err:
            logger.critical(f"{err}")
            return False
