import pytest
from httpx import HTTPStatusError
from services.starships_service import get_starships, get_starship_by_id
from tests.starships_tests.fixtures import mock_starship_data, mock_starships_data
from config import API_BASE_URL

ENDPOINT_API_URL = f"{API_BASE_URL}/starships"


@pytest.mark.asyncio
async def test_get_starships_success(httpx_mock, mock_starships_data):
    url = ENDPOINT_API_URL + "/"
    httpx_mock.add_response(url=url, json=mock_starships_data, status_code=200)

    result = await get_starships()
    assert result["count"] == 2
    assert len(result["starships"]) == 2
    assert result["starships"][0]["name"] == "CR90 corvette"
    assert result["starships"][1]["name"] == "Star Destroyer"


@pytest.mark.asyncio
async def test_get_starships_server_error(httpx_mock):
    url = ENDPOINT_API_URL + "/"
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_starships()
    assert exc_info.value.response.status_code == 500


@pytest.mark.asyncio
async def test_get_starship_by_id(httpx_mock, mock_starship_data):
    starship_id = 2
    url = f"{ENDPOINT_API_URL}/{starship_id}/"
    httpx_mock.add_response(url=url, json=mock_starship_data, status_code=200)

    result = await get_starship_by_id(starship_id)
    assert result["name"] == "CR90 corvette"
    assert result["model"] == "CR90 corvette"


@pytest.mark.asyncio
async def test_get_starship_by_id_not_found(httpx_mock):
    starship_id = 9999
    url = f"{ENDPOINT_API_URL}/{starship_id}/"
    httpx_mock.add_response(url=url, status_code=404)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_starship_by_id(starship_id)
    assert exc_info.value.response.status_code == 404


@pytest.mark.asyncio
async def test_get_starship_by_id_server_error(httpx_mock):
    starship_id = 1
    url = f"{ENDPOINT_API_URL}/{starship_id}/"
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_starship_by_id(starship_id)
    assert exc_info.value.response.status_code == 500
