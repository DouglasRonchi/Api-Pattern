from datetime import datetime
from uuid import uuid4
from mongoengine import Document, StringField, DateTimeField

from app.db.safe_document_mixing import SafeDocumentMixin


class Customer(Document, SafeDocumentMixin):

    id = StringField(required=True, unique=True, default=uuid4())
    name = StringField(required=True)
    created_at = DateTimeField(required=True, default=datetime.now())
    updated_at = DateTimeField()

    meta = {
        "collection": "customers",
        "indexes": ["id", "name"]
    }
