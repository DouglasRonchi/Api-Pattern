"""
Custom OpenApi Schema
"""
from fastapi.openapi.utils import get_openapi

from app.models.enums.api_type import ApiType


def custom_openapi():
    from app.main import app
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="1.0.0",
        openapi_version="3.0.2",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
        servers=[
            {"url": "http://127.0.0.1:8000"},
            {"url": "https://example.nonprod.com.br"}
        ]
    )
    set_x_techmetrics_tags(openapi_schema)
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def set_x_techmetrics_tags(openapi_schema):
    def set_x_techmetrics(endpoint: str, api_type: ApiType, domain: str) -> None:
        x_techmetrics = {"api_level": api_type, "api_domain": domain}
        openapi_schema["paths"][endpoint]["x-techmetrics"] = x_techmetrics

    # Custom x-techmetrics tag for each endpoint:
    set_x_techmetrics("/health", ApiType.public, "healthcheck")
    set_x_techmetrics("/healthcheck", ApiType.public, "healthcheck")

    set_x_techmetrics("/iceteam/v1/customers:paginated", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v1/customers", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v1/customers/{customer_id}:print", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v1/customers/{customer_id}", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v2/customers:paginated", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v2/customers", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v2/customers/{customer_id}:print", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v2/customers/{customer_id}", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v3/customers:paginated", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v3/customers", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v3/customers/{customer_id}:print", ApiType.corporate, "customer")
    set_x_techmetrics("/iceteam/v3/customers/{customer_id}", ApiType.corporate,"customer")

    set_x_techmetrics("/iceteam/v1/shipping-addresses", ApiType.corporate, "shipping-addresses")
    set_x_techmetrics("/iceteam/shipping-addresses", ApiType.corporate, "shipping-addresses")

    set_x_techmetrics("/iceteam/v1/invoices:long_process", ApiType.corporate, "invoices")
    set_x_techmetrics("/iceteam/invoices:long_process", ApiType.corporate, "invoices")

    set_x_techmetrics("/iceteam/v1/processes/{process_id}", ApiType.corporate, "processes")
    set_x_techmetrics("/iceteam/processes/{process_id}", ApiType.corporate, "processes")
