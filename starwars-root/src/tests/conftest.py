import pytest
from httpx import AsyncClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


@pytest.fixture
async def async_client():
    async with AsyncClient() as client:
        yield client
