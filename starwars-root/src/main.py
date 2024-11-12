from fastapi import FastAPI, HTTPException
from fastapi.exceptions import ResponseValidationError, RequestValidationError
from mangum import Mangum
import httpx
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import ValidationError
from .controllers import user_controller
from .controllers import films_controller
from .controllers import people_controller
from .controllers import planets_controller
from .controllers import species_controller
from .controllers import starships_controller
from .controllers import vehicles_controller
from .exception_handlers import (
    http_exception_handler,
    httpx_http_status_error_handler,
    starlette_http_exception_handler,
    httpx_request_error_handler,
    validation_exception_handler,
    response_validation_exception_handler,
    request_validation_exception_handler,
)

app = FastAPI(
    title="Power of Data - Star Wars Project",
    description="API para consulta de dados de filmes, personagens, planetas e naves de Star Wars",
    version="1.0.0",
    root_path="/dev",
)
handler = Mangum(app)

app.include_router(user_controller.router)
app.include_router(films_controller.router)
app.include_router(people_controller.router)
app.include_router(planets_controller.router)
app.include_router(species_controller.router)
app.include_router(starships_controller.router)
app.include_router(vehicles_controller.router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(httpx.HTTPStatusError, httpx_http_status_error_handler)
app.add_exception_handler(StarletteHTTPException, starlette_http_exception_handler)
app.add_exception_handler(httpx.RequestError, httpx_request_error_handler)
app.add_exception_handler(ValidationError, validation_exception_handler)
app.add_exception_handler(
    ResponseValidationError, response_validation_exception_handler
)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
