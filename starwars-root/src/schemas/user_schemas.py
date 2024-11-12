from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    message: str
    access_token: str


class RegisterRequest(BaseModel):
    email: str
    password: str


class RegisterResponse(BaseModel):
    message: str


class SafeUser(BaseModel):
    email: str
