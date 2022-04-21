import os
import unittest
from datetime import datetime

from mongoengine import disconnect, connect

from app.repository.customer import UserRepository
from app.schemas.customer import UserBase


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(db="iceteam", host="mongomock://localhost")

        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testsecretkey")
        os.environ.setdefault("MONGODB_URI", "test")

    def tearDown(self) -> None:
        disconnect()

    def test_user_repository_save(self):
        user = UserBase(email="test@example.com",
                        created_at=datetime(2020, 5, 2),
                        name="Test Name",
                        updated_at=datetime(2020, 5, 2))
        user = UserRepository().save(user)

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.created_at, datetime(2020, 5, 2, 0, 0))
        self.assertEqual(user.name, "Test Name")
        self.assertEqual(user.updated_at, datetime(2020, 5, 2, 0, 0))

    def test_user_repository_update(self):
        user = UserBase(email="test@example.com",
                        created_at=datetime(2020, 5, 2),
                        name="Test Name",
                        updated_at=datetime(2020, 5, 2))
        user_saved = UserRepository().save(user)
        user = UserBase(id=str(user_saved.id),
                        email="test@example.com",
                        created_at=datetime(2020, 5, 2),
                        name="Test Name Updated",
                        updated_at=datetime(2020, 5, 2))
        user = UserRepository().update(user)

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.created_at, datetime(2020, 5, 2, 0, 0))
        self.assertEqual(user.name, "Test Name Updated")
        self.assertEqual(user.updated_at, datetime(2020, 5, 2, 0, 0))

    def test_user_repository_update_with_no_user_on_database(self):
        user = UserBase(email="test@example.com",
                        created_at=datetime(2020, 5, 2),
                        name="Test Name",
                        updated_at=datetime(2020, 5, 2))
        user_saved = UserRepository().save(user)
        user = UserBase(id=str(user_saved.id),
                        email="test@example.com",
                        created_at=datetime(2020, 5, 2),
                        name="Test Name",
                        updated_at=datetime(2020, 5, 2))
        user_saved.delete()
        import pytest
        with pytest.raises(Exception) as err:
            UserRepository().update(user)

        self.assertEqual(err.typename, "CannotUpdateNotFoundUser")


if __name__ == '__main__':
    unittest.main()
