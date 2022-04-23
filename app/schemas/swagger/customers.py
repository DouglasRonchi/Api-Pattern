"""
Permissions Response Schema module
"""
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class Message(BaseModel):
    message: str


class CustomerResponseOK(BaseModel):
    id: str
    name: str
    created_at: datetime
    updated_at: datetime


class BadRequestPattern(BaseModel):
    type: str = "InvalidDate"
    error: str = "Data Inválida"
    detail: str = "Data de criação inválida"
    instance: str = "/customers/1"
    trace_id: str = "237462837462102342"


get_customer_by_id_responses = {
    200: {"model": CustomerResponseOK, "description": "When get all permissions successfully"},
    204: {"description": "Cannot find any customer on database"},
    404: {"model": Message, "description": "The permissions cannot be retrieved"},
    400: {"model": BadRequestPattern, "description": "Sending invalid data (data types, values)"}
}

create_new_customer_responses = {
    201: {"model": None, "description": "When customer was created successfully"},
    404: {"model": Message, "description": "Not Found"},
    400: {"model": BadRequestPattern, "description": "Sending invalid data (data types, values)"}
}
