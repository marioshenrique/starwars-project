import pytest
from fastapi import HTTPException
from src.services.user_services import (
    create_user,
    get_user_by_email,
    register_user,
    login,
)
from src.utils.security import verify_password
from src.models.user_model import User
from src.schemas.user_schemas import RegisterRequest, LoginRequest


def test_create_user_and_test_get_user_by_email(db_session):
    email = "alyrio99@gmail.com"
    password = "alyrio123"
    user = create_user(db_session, email, password)
    assert user.email == email
    assert verify_password(password, user.hashed_password) == True
    user_db = get_user_by_email(db_session, email)
    assert user_db is not None
    assert user_db.email == "alyrio99@gmail.com"


def test_register_user(db_session):
    # test register user
    register_request = RegisterRequest(email="alyrio99@gmail.com", password="alyrio123")
    response = register_user(db_session, register_request)
    assert response == {"message": f"{register_request.email} registered successfully"}

    db_user = (
        db_session.query(User).filter(User.email == register_request.email).first()
    )
    assert db_user is not None
    assert db_user.email == register_request.email

    # test register user with already registered email
    with pytest.raises(HTTPException) as exc_info:
        register_user(db_session, register_request)
    assert exc_info.value.status_code == 409
    assert exc_info.value.detail == "Email already registered"


def test_login_success(db_session):
    register_request = RegisterRequest(email="alyrio@gmail.com", password="alyrio123")
    register_user(db_session, register_request)
    login_request = LoginRequest(
        email=register_request.email, password=register_request.password
    )
    response = login(db_session, login_request)
    assert response["message"] == "Login successful"


def test_login_incorrect_email(db_session):
    login_request = LoginRequest(email="leigo@gmail.com", password="leigo123")
    with pytest.raises(HTTPException) as exc_info:
        login(db_session, login_request)
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "incorrect credentials"


def test_login_incorrect_password(db_session):
    register_request = RegisterRequest(email="alyrio@gmail.com", password="alyrio123")
    register_user(db_session, register_request)
    login_request = LoginRequest(email="alyrio@gmail.com", password="xxxxxxxx")
    with pytest.raises(HTTPException) as exc_info:
        login(db_session, login_request)
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "incorrect credentials"
