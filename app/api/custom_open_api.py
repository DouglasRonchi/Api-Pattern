from fastapi.openapi.utils import get_openapi


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
    app.openapi_schema = openapi_schema
    return app.openapi_schema
