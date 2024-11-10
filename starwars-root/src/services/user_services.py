import jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.user_model import User
from ..utils.security import hash_password
from ..config import SessionLocal, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from ..serializers.user_serializer import LoginRequest, RegisterRequest
from ..utils.security import verify_password


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def create_user(db: Session, email: str, password: str):
    hashed_password = hash_password(password)
    user = User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def register_user(db: Session, request: RegisterRequest):
    if get_user_by_email(db, request.email) is not None:
        raise HTTPException(status_code=409, detail="Email already registered")
    user = create_user(db, request.email, request.password)
    return {"message": f"{user.email} registered successfully"}


def login(db: Session, request: LoginRequest):
    user = get_user_by_email(db, request.email)
    if not user:
        raise HTTPException(status_code=401, detail="incorrect credentials")
    if not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="incorrect credentials")
    token = create_access_token(data={"sub": user.email})
    return {"message": "Login successful", "access_token": token}
