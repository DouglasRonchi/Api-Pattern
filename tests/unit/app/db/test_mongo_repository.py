"""
This is a test mongo repository module
"""
import unittest
from unittest.mock import patch

from app.database.mongo.mongo_repository import MongoDB


class TestMongoRepository(unittest.TestCase):
    @patch("app.db.mongo_repository.mongoengine")
    @patch("app.db.mongo_repository.AuthenticationSettings")
    def test_mongo_repository(self, mongoengine_mock, mongoconfigs_mock):
        MongoDB()
        assert mongoengine_mock.connect.called_once()
