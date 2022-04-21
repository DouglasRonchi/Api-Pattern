"""
This is a iceteam authentication settings module
"""
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    MONGODB_URI: str = Field("mongodb://root:example@localhost:27017/iceteam?authSource=admin", env="MONGODB_URI")
    SECRET_KEY_AUTH_SAML: str = Field("testsecretkey", env="SECRET_KEY_AUTH_SAML")
