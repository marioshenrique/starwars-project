from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import ResponseValidationError, RequestValidationError
import httpx
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel
from config import setup_logging

logger = setup_logging()


class ErrorResponse(BaseModel):
    detail: str


async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(exc.detail)
    return JSONResponse(
        status_code=exc.status_code, content=ErrorResponse(detail=exc.detail).dict()
    )


async def httpx_http_status_error_handler(request: Request, exc: httpx.HTTPStatusError):
    logger.error(f"External service returned an error")
    if exc.response.status_code == 404:
        detail = "Resource not found in external API"
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
    logger.error(f"Error type: {type(exc)}")
    if isinstance(exc, httpx.NetworkError):
        logger.error("Network error while connecting to external service.")
        status_code = 503
    elif isinstance(exc, httpx.ConnectTimeout):
        logger.error("Connection to external service timed out.")
        status_code = 504
    else:
        logger.error("An unexpected error occurred while contacting external service.")
        status_code = 500
    return JSONResponse(
        status_code=status_code,
        content=ErrorResponse(detail="Internal server error").dict(),
    )


async def response_validation_exception_handler(
    request: Request, exc: ResponseValidationError
):
    logger.error(f"Validation error in response: {exc.errors()}")
    print(f"Validation error in response: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            detail="An error occurred while validating the response data."
        ).dict(),
    )


async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    logger.error(f"Validation error in request: {exc.errors()}")
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            detail="An error occurred while validating the request data."
        ).dict(),
    )
