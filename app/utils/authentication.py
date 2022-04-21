from datetime import datetime, timedelta
from uuid import uuid4

import jwt
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from loguru import logger

from app.settings.settings import Settings

oauth2_scheme = HTTPBearer()


def decode_token(token):
    secret_key = Settings().SECRET_KEY_AUTH_SAML
    try:
        if "Bearer" in token:
            token = token.split()[-1]
        data = jwt.decode(token, secret_key, options={"verify_signature": False})
        return data

    except jwt.DecodeError:
        message = f"Token invalid {token} "
        logger.warning(message)

    except Exception as e:
        message = f"Something happened  - {e.args}"

    raise HTTPException(status_code=401,
                        detail=message,
                        headers={"WWW-Authenticate": "Bearer"})


def generate_token():
    try:
        date_now = datetime.utcnow()
        exp_date = date_now + timedelta(hours=4)
        token_settings = {
            'sub': str(uuid4()),
            'email': "",
            'iat': date_now,
            'exp': exp_date}
        access_token = jwt.encode(token_settings, Settings().SECRET_KEY_AUTH_SAML)
        return access_token

    except Exception as error:
        logger.error(f"Something happened on generator token {error.args}")
        return f"Something happened on generator token {error.args}"
