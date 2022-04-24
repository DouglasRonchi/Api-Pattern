from app.models.database.customer import Customer

customer_data = [{
    "name": "John Snow",
    "cpf": "12365478988",
    "city": "Winterfell",
    "created_at": "2022-04-13 18:14:31.972000",
    "updated_at": "2022-04-13 18:14:31.972000"
},
    {
        "name": "Daenerys Targaryen",
        "cpf": "98765432100",
        "city": "Dragonstone",
        "created_at": "2021-08-02 15:04:31.972000",
        "updated_at": "2022-01-15 00:14:31.972000"
    },
]


def load_customers_db_data():
    for customer in customer_data:
        Customer(**customer).save_safe()
