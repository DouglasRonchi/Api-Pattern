import os
import unittest

from mongoengine import connect, disconnect

from app.schemas.customer import CustomerSchema
from app.services.customer import CustomerService


class TestPermissionsService(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(db="iceteam", host="mongomock://localhost")

        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testsecretkey")
        os.environ.setdefault("MONGODB_URI", "test")

    def tearDown(self) -> None:
        disconnect()

    def test_when_create_a_new_customer_must_return_object_created(self):
        data = {
            "name": "Jonh",
            "cpf": "12365478988",
            "city": "Chinatown",
            "created_at": "2022-02-02",
            "updated_at": "2022-02-02",
        }
        customer = CustomerSchema(**data)

        response = CustomerService().create_new_customer(customer)

        self.assertTrue(response.id)
        self.assertEqual("Jonh", response.name)
        self.assertEqual("12365478988", response.cpf)
        self.assertEqual("Chinatown", response.city)
        self.assertEqual("2022-02-02", response.created_at)
        self.assertEqual("2022-02-02", response.updated_at)


if __name__ == '__main__':
    unittest.main()
