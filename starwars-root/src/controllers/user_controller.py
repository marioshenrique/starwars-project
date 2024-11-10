from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..serializers.user_serializer import LoginRequest, RegisterRequest
from ..config import SessionLocal
from ..services.user_services import login, register_user
from ..dependencies.database_dependencies import get_db

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login")
async def login_user(request: LoginRequest = Depends(), db: Session = Depends(get_db)):
    return login(db, request)


@router.post("/register")
async def register(request: RegisterRequest = Depends(), db: Session = Depends(get_db)):
    return register_user(db, request)