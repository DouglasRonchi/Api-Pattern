import unittest
import pytest
from mongoengine import disconnect, connect

from app.models.database.customer import Customer


class TestCustomerModel(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(db="mongomock", host="mongomock://localhost")
        user = Customer()
        user.email = 'mario@test.com.br'
        user.save_safe()

    def tearDown(self) -> None:
        disconnect()

    def test_email_duplicated_save(self):
        user = Customer()
        user.email = "mario@test.com.br"
        with pytest.raises(Exception) as err:
            user.save_safe(user)

        assert err.typename == "NotUniqueError"


if __name__ == '__main__':
    unittest.main()
