"""
Schema for Customer
"""
from datetime import datetime

import pendulum
from pendulum.parsing import ParserError
from pydantic import BaseModel, Field, validator
from typing import Optional

id_description = "Customer identification code."
name_description = "The Customer Name. String format."
age_description = "The Customer Age. Integer format."
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
    age: Optional[int] = Field(example=22, description=age_description)
    cpf: Optional[str] = Field(example="12345645600", description=cpf_description)
    city: Optional[str] = Field(example="Test City", description=city_description)
    created_at: str = Field(example=datetime.now(), default=datetime.now(), description=created_at_description)
    updated_at: Optional[str] = Field(example=datetime.now(), description=updated_at_description)

    # @validator('cpf')
    # def cpf_must_contain_eleven_max_characters(cls, cpf):
    #     if len(cpf) != 11:
    #         raise ValueError("Cpf must contain exactly eleven characters")
    #     return cpf

    @validator('created_at')
    def passwords_match(cls, created_at):
        try:
            parsed_date = pendulum.parse(created_at)
        except ParserError as err:
            raise ValueError('Unable to parse date. Invalid date format')
        if parsed_date.age > 100:
            raise ValueError('Invalid date format')
        return created_at

    # @validator('updated_at')
    # def username_alphanumeric(cls, updated_at):
    #     if True:
    #
    #     return updated_at