from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .database_dependencies import get_db
from jose import jwt, JWTError
from ..config import SECRET_KEY, ALGORITHM
from ..models.user_model import User
from ..serializers.user_serializer import SafeUser

bearer_scheme = HTTPBearer()


def get_client_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email: str = payload.get("sub")
        if user_email is None:
            raise HTTPException(
                status_code=401, detail="Could not validate credentials"
            )
        user = db.query(User).filter(User.email == user_email).first()
        if user is None:
            raise HTTPException(
                status_code=401, detail="Could not validate credentials"
            )
        return SafeUser(email=user_email)
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
