import os
import unittest
from http import HTTPStatus
from unittest.mock import patch, Mock

from fastapi.testclient import TestClient
from mongoengine import disconnect, connect

os.environ.setdefault("MONGODB_URI", "test")


class TestEndpoint(unittest.TestCase):
    def setUp(self) -> None:
        from app.main import app
        disconnect()
        self.client = TestClient(app)
        connect(db="mongomock", host="mongomock://localhost")

    def tearDown(self) -> None:
        disconnect()

    @patch('app.endpoints.customers_v1.Depends')
    @patch('app.endpoints.customers_v1.decode_token')
    def test_when_get_all_customers_should_return_200(self,
                                                      decode_token_mock,
                                                      depends_mock):
        response = self.client.get("iceteam/v1/customers:paginated")
        self.assertEqual(HTTPStatus.OK, response.status_code)

    @patch('app.endpoints.customers_v1.Depends')
    @patch('app.endpoints.customers_v1.decode_token')
    def test_when_get_all_customers_paginated_should_return_expected_keys(self,
                                                                          decode_token_mock,
                                                                          depends_mock):
        response = self.client.get("iceteam/v1/customers:paginated")
        self.assertEqual(['data', 'current_page', 'total_items', 'total_pages'],
                         list(response.json().keys()))


if __name__ == '__main__':
    unittest.main()
