"""
This is a processes' endpoint module

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

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse
from app.utils.authentication import oauth2_scheme, decode_token
from loguru import logger

processes_endpoint_v1_router = APIRouter()


@processes_endpoint_v1_router.get('/processes/{process_id}')
def get_process_status_by_id(process_id):
    """
    Used to get status of a process by process_id
    :return: 200 - Status of process
    """
    try:
        # decode_token(token.credentials)
        # TODO just to show how was the returns: Must be removed: Need to Implement
        response = make_fake_process_response(process_id)
        return JSONResponse(status_code=http.HTTPStatus.OK, content=response)
    except Exception as err:
        logger.error(f"{err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})


# TODO just to show how was the returns: Must be removed: Need to Implement
def make_fake_process_response(process_id):
    if process_id == "1":
        status, percentual = "running", 40
    elif process_id == "2":
        status, percentual = "completed", 100
    else:
        status, percentual = "running", 10
    response = {
        "process_id": process_id,
        "status": status,
        "percentual": percentual
    }
    return response
