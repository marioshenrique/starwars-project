from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.user_schemas import (
    LoginRequest,
    RegisterRequest,
    LoginResponse,
    RegisterResponse,
)
from config import SessionLocal
from services.user_services import login, register_user
from dependencies.database_dependencies import get_db

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login", response_model=LoginResponse)
async def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    return login(db, request)


@router.post("/register", response_model=RegisterResponse)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(db, request)
