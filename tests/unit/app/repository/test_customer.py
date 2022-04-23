import os
import unittest

from mongoengine import disconnect, connect


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(db="iceteam", host="mongomock://localhost")

        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testsecretkey")
        os.environ.setdefault("MONGODB_URI", "test")

    def tearDown(self) -> None:
        disconnect()


if __name__ == '__main__':
    unittest.main()
