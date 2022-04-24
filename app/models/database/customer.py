from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, IntField

from app.db.mongo.mongo_safe_document import SafeDocument


class Customer(Document, SafeDocument):
    name = StringField(required=True)
    age = IntField(required=False)
    cpf = StringField(required=True, unique=True, max_length=11)
    city = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    updated_at = DateTimeField(required=True)

    meta = {
        "collection": "customers",
        "indexes": ["name"]
    }
