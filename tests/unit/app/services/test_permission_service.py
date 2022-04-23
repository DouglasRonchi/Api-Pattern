import os
import unittest

import pytest
from mongoengine import connect, disconnect

from app.models.database.permission import Permission
from app.models.database.session import Session
from app.models.database.customer import User
from app.services.customer import PermissonService
from tests.db_test_data.customers import load_db_data, create_example_expired_token, user_data


class TestPermissionsService(unittest.TestCase):
    def setUp(self) -> None:
        disconnect()
        connect(db="iceteam", host="mongomock://localhost")

        os.environ.setdefault("SECRET_KEY_AUTH_SAML", "testsecretkey")
        os.environ.setdefault("MONGODB_URI", "test")
        load_db_data()

    def tearDown(self) -> None:
        disconnect()

    def test_get_user_all(self):
        response = PermissonService().get_all_user_permissions()
        assert len(response.get('data')) == 2

    def test_get_user_all_expired_token(self):
        disconnect()
        connect(db="iceteam", host="mongomock://localhost")
        user = User(**user_data[0]).save_safe()

        example_encoded_token = create_example_expired_token(user.email)
        session = Session()
        session.client_id = '87bcad5e-ea8f-429b-8b54-5d8be6bab9ea'
        session.user = user
        session.token = example_encoded_token
        session.exp_date = "2022-04-13 18:14:31.972000"
        session.email = user.email
        session.save_safe()

        permission = Permission()
        permission.user = user
        permission.frontend = {"permissions": ["admin"]}
        permission.rsc = {"rsc_id": 10, "permissions": ["backoffice", "technician"]}
        permission.frontend = {"permissions": ["admin"]}
        permission["iceteam-lending-prioritization"] = {"permissions": ["admin"]}
        permission.save_safe()

        response = PermissonService().get_all_user_permissions()
        assert len(response.get('data')) == 1

    def test_get_user_delete_all(self):
        users = User.objects().all()
        for user in users:
            user.delete()
        with pytest.raises(Exception) as err:
            PermissonService().get_all_user_permissions()
        assert err.typename == "NotFoundAnyUser"

    def test_get_user_delete_all_sessions(self):
        users = User.objects().all()
        for user in users:
            session = Session.objects(email=user.email).first()
            session.delete()

        response = PermissonService().get_all_user_permissions()

        self.assertEqual(response["data"][0]["last_logon_at"], "")
        self.assertEqual(response["data"][1]["last_logon_at"], "")

    def test_get_user_all_decode_error_token(self):
        disconnect()
        connect(db="iceteam", host="mongomock://localhost")
        user = User(**user_data[0]).save_safe()

        session = Session()
        session.client_id = '87bcad5e-ea8f-429b-8b54-5d8be6bab9ea'
        session.user = user
        session.token = ""
        session.exp_date = "2022-04-13 18:14:31.972000"
        session.email = user.email
        session.save_safe()

        permission = Permission()
        permission.user = user
        permission.frontend = {"permissions": ["admin"]}
        permission.rsc = {"rsc_id": 10, "permissions": ["backoffice", "technician"]}
        permission.frontend = {"permissions": ["admin"]}
        permission["iceteam-lending-prioritization"] = {"permissions": ["admin"]}
        permission.save_safe()

        response = PermissonService().get_all_user_permissions()
        assert len(response.get('data')) == 1


if __name__ == '__main__':
    unittest.main()
