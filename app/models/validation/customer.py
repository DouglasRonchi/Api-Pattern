from datetime import datetime

from pydantic import BaseModel, Field


class Customer(BaseModel):
    id: str = Field(description="Customer identification code")
    name: str = Field(description="The Customer Name")
    cpf: str = Field(description="Customer CPF number. Enter only the numbers, "
                                 "without dots and dash (12345678900, for example). Required field.")
    city: str = Field(description="Customer city. Enter only string.")
    created_at: datetime = Field(description="Customer's register created at. Use the YYYY-MM-DD format (1998-07-23,"
                                             " for example). The date must be less than today's date and greater"
                                             " than 1900-01-01. Required field.")
    updated_at: datetime = Field(description="Customer's register updated at. Use the YYYY-MM-DD format (1998-07-23, "
                                             "for example). The date must be less than today's date and greater"
                                             " than 1900-01-01. Required field.")