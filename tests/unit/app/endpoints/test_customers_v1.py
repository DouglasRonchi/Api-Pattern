import os
import unittest
from http import HTTPStatus

from fastapi.testclient import TestClient
from mongoengine import disconnect, connect

from app.utils.authentication import generate_token

os.environ.setdefault("MONGODB_URI", "test")


class TestCustomerEndpoints(unittest.TestCase):
    def setUp(self) -> None:
        from app.main import app
        self.client = TestClient(app)
        disconnect()
        connect(db="mongomock", host="mongomock://localhost")
        self.authentication_token = generate_token("test@test.com")

    def tearDown(self) -> None:
        disconnect()

    def test_when_get_all_customers_should_return_200(self):
        response = self.client.get("iceteam/v1/customers:paginated",
                                   headers={"Authorization": self.authentication_token})
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_when_get_all_customers_paginated_should_return_expected_keys(self):
        response = self.client.get("iceteam/v1/customers:paginated",
                                   headers={"Authorization": self.authentication_token})
        print(response.json())
        self.assertEqual(['data', 'current_page', 'total_items', 'total_pages'],
                         list(response.json().keys()))

    def test_when_sent_valid_data_should_return_201_created(self):
        data = {
            "name": "John",
            "cpf": "12345678999",
            "city": "SomeCity",
            "created_at": "2022-02-02",
            "updated_at": "2022-02-02",
        }
        response = self.client.post("iceteam/v1/customers",
                                    headers={"Authorization": self.authentication_token},
                                    json=data)
        self.assertEqual(HTTPStatus.CREATED, response.status_code)

    def test_when_sent_some_invalid_date_type_should_return_422(self):
        data = {
            "name": "John",
            "cpf": "12345678999",
            "city": "SomeCity",
            "created_at": "abc",
            "updated_at": "2022-02-02",
        }
        response = self.client.post("iceteam/v1/customers",
                                    headers={"Authorization": self.authentication_token},
                                    json=data)
        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
        self.assertEqual({'detail': [{'loc': ['body', 'created_at'],
                                      'msg': 'Unable to parse date. Invalid date format',
                                      'type': 'value_error'}]}, response.json())

    def test_when_sent_some_invalid_date_should_return_422(self):
        data = {
            "name": "John",
            "cpf": "12345678999",
            "city": "SomeCity",
            "created_at": "1700-02-02",
            "updated_at": "2022-02-02",
        }
        response = self.client.post("iceteam/v1/customers",
                                    headers={"Authorization": self.authentication_token},
                                    json=data)
        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
        self.assertEqual({'detail': [{'loc': ['body', 'created_at'],
                                      'msg': 'Invalid date format',
                                      'type': 'value_error'}]}, response.json())

    def test_when_sent_a_string_value_in_a_numeric_field_should_return_422(self):
        data = {
            "name": "Jonh",
            "age": "Twenty",
            "cpf": "12345678999",
            "city": "SomeCity",
            "created_at": "2022-02-02",
            "updated_at": "2022-02-02",
        }
        response = self.client.post("iceteam/v1/customers",
                                    headers={"Authorization": self.authentication_token},
                                    json=data)
        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
        self.assertEqual({'detail': [{'loc': ['body', 'age'],
                                      'msg': 'value is not a valid integer',
                                      'type': 'type_error.integer'}]}, response.json())

    def test_when_user_not_authenticated_should_return_401(self):
        os.environ.clear()
        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "test")
        authentication_token = generate_token()
        os.environ.clear()
        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testsecretkey")
        response = self.client.get("iceteam/v1/customers:paginated",
                                   headers={"Authorization": authentication_token})
        self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)

    def test_when_denied_access_to_operation_or_resource_or_not_authorized_to_access_should_return_403(self):
        authentication_token = generate_token("")
        response = self.client.get("iceteam/v1/customers:paginated",
                                   headers={"Authorization": authentication_token})
        self.assertEqual(HTTPStatus.FORBIDDEN, response.status_code)

    def test_when_recurse_not_found_should_return_404(self):
        response = self.client.get("iceteam/v1/places")
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    # TODO Server processing error 500 - Server error TEST


if __name__ == '__main__':
    unittest.main()
