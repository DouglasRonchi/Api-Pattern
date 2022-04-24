"""
This is a shipping addresses endpoint module

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

from app.exceptions.exceptions import UnauthorizedException, ForbiddenException
from app.utils.authentication import oauth2_scheme, decode_token
from loguru import logger

shipping_addresses_endpoint_v1_router = APIRouter()


@shipping_addresses_endpoint_v1_router.get('/shipping-addresses')
def get_all_shipping_addresses(token: any = Depends(oauth2_scheme)):
    """
    just to show if there is any composite name,
    it must be in lower case, separated by a hyphen (-).
    :return:
    """
    try:
        decode_token(token.credentials)
        data = {"shipping-addresses": "various"}
        return JSONResponse(status_code=http.HTTPStatus.OK, content=data)
    except UnauthorizedException:
        return JSONResponse(status_code=http.HTTPStatus.UNAUTHORIZED, content={"message": "Unauthorized to access"})
    except ForbiddenException:
        return JSONResponse(status_code=http.HTTPStatus.FORBIDDEN, content={"message": "Access denied"})
    except Exception as err:
        logger.error(f"{err}")
        return JSONResponse(status_code=http.HTTPStatus.BAD_REQUEST, content={"message": "Something went wrong"})
