from app.models.database.customer import User

user_data = [{
    "id": "625713cf97407a8c846e51e9",
    "name": "Zé Tecnico",
    "email": "test@test.com",
    "created_at": "2022-04-13 18:14:31.972000",
    "updated_at": "2022-04-13 18:14:31.972000"
},
    {
        "id": "625713cf97407a8c846e5110",
        "name": "Mario Tecnico",
        "email": "mario@test.com",
        "created_at": "2021-08-02 15:04:31.972000",
        "updated_at": "2022-01-15 00:14:31.972000"
    },
]


def load_db_data():
    for user in user_data:
        user = User(**user).save_safe()

        example_encoded_token = create_example_valid_token(user.email)
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


