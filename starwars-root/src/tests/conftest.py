import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Base
from models.user_model import User
from httpx import AsyncClient


@pytest.fixture
async def async_client():
    async with AsyncClient() as client:
        yield client


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
