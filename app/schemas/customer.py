"""
Schema for Customer
"""
from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional

id_description = "Customer identification code"
name_description = "The Customer Name"
cpf_description = "Customer CPF number. Enter only the numbers, without dots and dash (12345678900, for example). " \
                  "Required field. "
city_description = "Customer city. Enter only string."
created_at_description = "Customer's register created at. Use the YYYY-MM-DD format (1998-07-23, for example). The " \
                         "date must be less than today's date and greater than 1900-01-01. Required field. "
updated_at_description = "Customer's register updated at. Use the YYYY-MM-DD format (1998-07-23, for example). The " \
                         "date must be less than today's date and greater than 1900-01-01. Required field. "


class CustomerSchema(BaseModel):
    """
    Common fields of Customer
    """
    name: str = Field(example="Test Name", description=name_description)
    cpf: Optional[str] = Field(example="12345645600", description=cpf_description)
    city: Optional[str] = Field(example="Test City", description=city_description)
    created_at: datetime = Field(example=datetime.now(), default=datetime.now(), description=created_at_description)
    updated_at: Optional[datetime] = Field(example=datetime.now(), description=updated_at_description)
