from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import ResponseValidationError, RequestValidationError
import httpx
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    detail: str


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code, content=ErrorResponse(detail=exc.detail).dict()
    )


async def httpx_http_status_error_handler(request: Request, exc: httpx.HTTPStatusError):
    if exc.response.status_code == 404:
        detail = "Resource not found"
    else:
        detail = "Error fetching data from external service"
    return JSONResponse(
        status_code=exc.response.status_code,
        content=ErrorResponse(detail=detail).dict(),
    )


async def starlette_http_exception_handler(
    request: Request, exc: StarletteHTTPException
):
    return JSONResponse(
        status_code=exc.status_code, content=ErrorResponse(detail=exc.detail).dict()
    )


async def httpx_request_error_handler(request: Request, exc: httpx.RequestError):
    return JSONResponse(
        status_code=503,
        content=ErrorResponse(detail="External service unavailable").dict(),
    )


async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400, content=ErrorResponse(detail="Validation error").dict()
    )


async def response_validation_exception_handler(
    request: Request, exc: ResponseValidationError
):
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            detail="There was an error validating the response data."
        ).dict(),
    )


async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=400, content=ErrorResponse(detail=str(exc.errors())).dict()
    )
