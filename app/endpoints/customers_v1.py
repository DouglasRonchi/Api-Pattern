"""
This is a customers' endpoint module

From an API point of view, controlling versioning is relatively simple.
But making this control in order to avoid compatibility breaks in the backend is quite complex.

A - You should avoid breaking compatibility with the current version.
    Every break is a potential source of problems and adjustments.
B - New versions of the backend service do not necessarily impact new API versions. These versions run independently.
C - A shutdown/support policy for previous versions must be defined.
    For example: Only the last two released versions of some API will have bug fixes/support.
D - A deadline must be defined for the migration of clients that use some old version to the newest one.
"""

import http
from math import ceil
from typing import Optional

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from app.models.validation.customer import Customer
from app.schemas.swagger.customers import get_customer_by_id_responses
from app.utils.authentication import oauth2_scheme, decode_token
from loguru import logger

customers_endpoint_v1_router = APIRouter()
# TODO 02 : REMOVE : Tricky to create v2 and v3 - Just for template (ref TODO 03)
customers_endpoint_v2_router = customers_endpoint_v1_router
customers_endpoint_v3_router = customers_endpoint_v1_router


@customers_endpoint_v1_router.get('/customers:paginated')
def get_all_customers_paginated(_order: str = "",
                                _page: int = 1,
                                _size: Optional[int] = 10):
    """
    Returns to the 1st page of the customer collection
    :param _page: Set the current page, default is 1. type: int
    :param _size: Set the page size, the size of items in the page, default is 10. type: int
    :param _order: If the ordering direction of some attribute is not informed, asc will be used by default. type: str
                    Eg. _order="name asc, created_at desc"
    :return:
    """
    try:
        # decode_token(token.credentials)
        data = [
            {"id", 1},
            {"id", 2}
        ]
        data = {
            "data": [],
            "current_page": _page,
            "total_items": len(data),
            "total_pages": ceil(len(data) / _size)
        }
        return JSONResponse(status_code=http.HTTPStatus.OK, content=data)
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})


@customers_endpoint_v1_router.get('/customers')
def get_all_customers():
    """
    Returns to the 1st page of the customer collection
    :return:
    """
    try:
        # decode_token(token.credentials)
        data = {}
        return JSONResponse(status_code=http.HTTPStatus.OK, content=data)
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})


@customers_endpoint_v1_router.get('/customers/{customer_id}:print')
def print_customer_on_old_printer():
    """
    Actions like (:print) must be before the common get_by_id (/customers/{customer_id})
    Make a custom action, in this case "print".
    :return:
    """
    try:
        # decode_token(token.credentials)
        data = {"action": "Printing customer on an old printer"}
        return JSONResponse(status_code=http.HTTPStatus.OK, content=data)
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})


@customers_endpoint_v1_router.get('/customers/{customer_id}', responses=get_customer_by_id_responses)
def get_customer_by_id(customer_id):
    """
    Returns the client with the id on the params {customer_id}
    :param customer_id: The customer id. type: str(uuid4)
    :return:
    """
    try:
        # decode_token(token.credentials)
        # TODO just to show * Idempotence *: Must be removed: Need to Implement
        data = get_fake_customer(customer_id)
        return JSONResponse(status_code=http.HTTPStatus.OK, content=data)
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})


# TODO just to show * Idempotence *: Must be removed: Need to Implement
def get_fake_customer(customer_id):
    if customer_id == "1":
        data = {"id": customer_id,
                "name": "customer name",
                "created_at": "2022-04-21T12:20:15.123Z",
                "updated_at": "2022-04-21T12:20:15.123Z",
                }
    else:
        data = {}
    return data


@customers_endpoint_v1_router.post('/customers')
def create_new_customer(customer: Customer):
    """
    Create a new customer and add it to the customers collection
    :return:
    """
    try:
        # decode_token(token.credentials)
        # Create New Customer
        return JSONResponse(status_code=http.HTTPStatus.CREATED)
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})


@customers_endpoint_v1_router.put('/customers/{customer_id}')
def update_all_customer_fields(customer_id):
    """
    Changes all customer fields except id,
    according to the values that are passed in the body of the request.
    Fields that are not passed will be considered null.
    :param customer_id: The customer id. type: str(uuid4)
    :return:
    """

    try:
        # decode_token(token.credentials)
        data = {customer_id: customer_id}
        return JSONResponse(status_code=http.HTTPStatus.OK, content=data)
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})


@customers_endpoint_v1_router.patch('/customers/{customer_id}')
def update_specific_customer_fields(customer_id):
    """
    Change only the fields passed in the request.
    ATTENTION: The format of the JSON passed must follow the standard defined in RFC6902
    :param customer_id: The customer id. type: str(uuid4)
    :return:
    """
    try:
        # decode_token(token.credentials)
        # Update fields that comes from body
        return JSONResponse(status_code=http.HTTPStatus.OK)
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})


@customers_endpoint_v1_router.delete('/customers/{customer_id}')
def delete_customer_by_id(customer_id):
    """
    Delete customer by customer id
    :param customer_id: The customer id. type: str(uuid4)
    :return:
    """
    try:
        # decode_token(token.credentials)
        # Delete customer by id
        return JSONResponse(status_code=http.HTTPStatus.OK)
    except Exception as err:
        logger.error(f"Error {err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})
