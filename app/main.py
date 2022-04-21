"""
This is a main API module
"""
from fastapi import FastAPI

from app.api.custom_open_api import custom_openapi
from app.db.mongo_repository import MongoDB
from app.endpoints.customers_v1 import customers_endpoint_v1_router, customers_endpoint_v2_router, \
    customers_endpoint_v3_router
from app.endpoints.invoices_v1 import invoices_endpoint_v1_router
from app.endpoints.processes_v1 import processes_endpoint_v1_router
from app.endpoints.shipping_addresses_v1 import shipping_addresses_endpoint_v1_router
from app.healthchecks.endpoint_healthcheck import health_check_router
from app.models.enums.api_type import ApiType
from loguru import logger

# TODO Add this extra infos to openapi.json:

extra_infos = {
    "x-techmetrics": {
        "api_level": ApiType.corporate,
        "api_domain": "iceteam"
    }
}


logger.info(f"Starting API")
app = FastAPI(title="API Rest Project Template")  # TODO 01 Put the name of your project here.


@app.on_event("startup")
async def create_db_client():
    try:
        MongoDB()
    except Exception as err:
        logger.error(f'{err}')

# Add all the routes
app.include_router(health_check_router, tags=["HealthCheck"])

app.include_router(customers_endpoint_v1_router, prefix="/iceteam/v1", tags=["Customers"], deprecated=True)
app.include_router(customers_endpoint_v2_router, prefix="/iceteam/v2", tags=["Customers"])  # Have bug fixes/support.
app.include_router(customers_endpoint_v3_router, prefix="/iceteam/v3", tags=["Customers"])  # Have bug fixes/support.
# TODO 03 If the version number is not informed, the Last Released version will be used:
app.include_router(customers_endpoint_v3_router, prefix="/iceteam", tags=["Customers"])

app.include_router(shipping_addresses_endpoint_v1_router, prefix="/iceteam/v1", tags=["Shipping Addresses"])
app.include_router(shipping_addresses_endpoint_v1_router, prefix="/iceteam", tags=["Shipping Addresses"])

app.include_router(invoices_endpoint_v1_router, prefix="/iceteam/v1", tags=["Invoices"])
app.include_router(invoices_endpoint_v1_router, prefix="/iceteam", tags=["Invoices"])

app.include_router(processes_endpoint_v1_router, prefix="/iceteam/v1", tags=["Processes"])
app.include_router(processes_endpoint_v1_router, prefix="/iceteam", tags=["Processes"])

app.openapi = custom_openapi
