from fastapi import APIRouter, Depends, status
from ..serializers.user_serializer import LoginRequest, RegisterRequest
from ..services.user_services import login, register_user

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login")
async def login_user(request: LoginRequest):
    return login(request)

@router.post("/register")
async def register(request: RegisterRequest):
    return register_user(request)