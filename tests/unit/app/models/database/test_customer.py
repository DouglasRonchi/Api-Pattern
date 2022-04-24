import unittest
from datetime import datetime

import pytest
from mongoengine import disconnect, connect

from app.models.database.customer import Customer


class TestCustomerModel(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(db="mongomock", host="mongomock://localhost")
        user = Customer()
        user.name = "mario"
        user.email = "mario@test.com.br"
        user.cpf = "12345678988"
        user.city = "Chinatown"
        user.created_at = datetime(2022, 2, 2)
        user.updated_at = datetime(2022, 2, 2)
        user.save_safe()

    def tearDown(self) -> None:
        disconnect()

    def test_when_save_a_new_customer_with_email_duplicated(self):
        user = Customer()
        user.name = "mario"
        user.email = "mario@test.com.br"
        user.cpf = "12345678988"
        user.city = "Chinatown"
        user.created_at = datetime(2022, 2, 2)
        user.updated_at = datetime(2022, 2, 2)
        with pytest.raises(Exception) as err:
            user.save_safe(user)

        assert err.typename == "NotUniqueError"

    def test_when_save_a_new_customer_with_cpf_duplicated(self):
        user = Customer()
        user.name = "mario"
        user.email = "mariotest@test.com.br"
        user.cpf = "12345678988"
        user.city = "Chinatown"
        user.created_at = datetime(2022, 2, 2)
        user.updated_at = datetime(2022, 2, 2)
        with pytest.raises(Exception) as err:
            user.save_safe(user)

        assert err.typename == "NotUniqueError"


if __name__ == '__main__':
    unittest.main()
