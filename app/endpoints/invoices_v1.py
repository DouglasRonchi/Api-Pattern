"""
This is an invoices' endpoint module

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
from uuid import uuid4

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from app.exceptions.exceptions import UnauthorizedException, ForbiddenException
from app.utils.authentication import oauth2_scheme, decode_token
from loguru import logger

invoices_endpoint_v1_router = APIRouter()


@invoices_endpoint_v1_router.get('/invoices:long_process')
def eg_long_process(token: any = Depends(oauth2_scheme)):
    """
    Long processes are usually called asynchronously, that is: The server receives the
    call and processes it independently, without the client being "stuck" waiting for the response.
    :long_process Could be some types of long processes:
    - heavy processes that aren't needed answers immediate or that will generate competition at peak times;
    - De-prioritized information, i.e. information that can be returned outside peak hours;
    - Processing requiring manual validation;
    - Processing that require a chain of prerequisites from the which are not available at the time of request;
    :return: 202 - Accepted response with Location header
    """
    try:
        decode_token(token.credentials)
        location_header = {"Location": f"iceteam/v1/processes/{str(uuid4())}"}
        return JSONResponse(status_code=http.HTTPStatus.ACCEPTED, headers=location_header)
    except UnauthorizedException:
        return JSONResponse(status_code=http.HTTPStatus.UNAUTHORIZED, content={"message": "Unauthorized to access"})
    except ForbiddenException:
        return JSONResponse(status_code=http.HTTPStatus.FORBIDDEN, content={"message": "Access denied"})
    except Exception as err:
        logger.error(f"{err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})
