from fastapi import HTTPException
from starlette.responses import JSONResponse

def http_exception_handler(app):
    @app.exception_handler(HTTPException)
    async def http_exception(request, exc):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": f"HTTPException: {exc.detail}"}
        )

def generic_exception_handler(app):
    @app.exception_handler(Exception)
    async def generic_exception(request, exc):
        return JSONResponse(
            status_code=500,
            content={"message": "Internal server error"}
        )
