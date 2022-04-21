"""
Schema for Customer
"""
from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional


class CustomerBase(BaseModel):
    """
    Common fields of Customer
    """
    id: str = Field(example="123456789abcdefg")
    name: str = Field(example="Test Name")
    created_at: datetime = Field(example=datetime.now(), default=datetime.now())
    updated_at: Optional[datetime] = Field(example=datetime.now())


class CustomerSchema(CustomerBase):
    """
    Properties to return with all attributes
    """
