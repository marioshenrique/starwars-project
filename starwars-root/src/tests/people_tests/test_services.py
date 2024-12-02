import pytest
from httpx import HTTPStatusError
from services.people_service import get_peoples, get_people_by_id
from fixtures import mock_people_data, mock_peoples_data
from config import API_BASE_URL

ENDPOINT_API_URL = f"{API_BASE_URL}/people"


@pytest.mark.asyncio
async def test_get_peoples_success(httpx_mock, mock_peoples_data):
    url = ENDPOINT_API_URL
    httpx_mock.add_response(url=url, json=mock_peoples_data, status_code=200)

    result = await get_peoples()
    assert result["count"] == 2
    assert len(result["peoples"]) == 2
    assert result["peoples"][0]["name"] == "Luke Skywalker"
    assert result["peoples"][1]["name"] == "C-3PO"


@pytest.mark.asyncio
async def test_get_peoples_server_error(httpx_mock):
    url = ENDPOINT_API_URL
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_peoples()
    assert exc_info.value.response.status_code == 500


@pytest.mark.asyncio
async def test_get_people_by_id_success(httpx_mock, mock_people_data):
    people_id = 1
    url = f"{ENDPOINT_API_URL}/{people_id}/"
    httpx_mock.add_response(url=url, json=mock_people_data, status_code=200)

    result = await get_people_by_id(people_id)
    assert result["name"] == "Luke Skywalker"
    assert result["height"] == "172"
    assert result["mass"] == "77"


@pytest.mark.asyncio
async def test_get_people_by_id_not_found(httpx_mock):
    people_id = 9999
    url = f"{ENDPOINT_API_URL}/{people_id}/"
    httpx_mock.add_response(url=url, status_code=404)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_people_by_id(people_id)
    assert exc_info.value.response.status_code == 404


@pytest.mark.asyncio
async def test_get_people_by_id_server_error(httpx_mock):
    people_id = 1
    url = f"{ENDPOINT_API_URL}/{people_id}/"
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_people_by_id(people_id)
    assert exc_info.value.response.status_code == 500
