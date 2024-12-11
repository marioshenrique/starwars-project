import pytest
from httpx import HTTPStatusError
from services.vehicles_service import get_vehicles, get_vehicle_by_id
from tests.vehicles_tests.fixtures import mock_vehicle_data, mock_vehicles_data
from config import API_BASE_URL

ENDPOINT_API_URL = f"{API_BASE_URL}/vehicles"


@pytest.mark.asyncio
async def test_get_vehicles_success(httpx_mock, mock_vehicles_data):
    url = ENDPOINT_API_URL
    httpx_mock.add_response(url=url, json=mock_vehicles_data, status_code=200)

    result = await get_vehicles()
    assert result["count"] == 2
    assert result["vehicles"][0]["name"] == "Sand Crawler"
    assert result["vehicles"][1]["name"] == "T-16 skyhopper"
    assert len(result["vehicles"]) == 2


@pytest.mark.asyncio
async def test_get_vehicles_server_error(httpx_mock):
    url = ENDPOINT_API_URL
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_vehicles()
    assert exc_info.value.response.status_code == 500


@pytest.mark.asyncio
async def test_get_vehicles_by_id_success(httpx_mock, mock_vehicle_data):
    vehicle_id = 4
    url = f"{ENDPOINT_API_URL}/{vehicle_id}/"
    httpx_mock.add_response(url=url, json=mock_vehicle_data, status_code=200)

    result = await get_vehicle_by_id(vehicle_id)
    assert result["name"] == "Sand Crawler"
    assert result["model"] == "Digger Crawler"
    assert result["manufacturer"] == "Corellia Mining Corporation"


@pytest.mark.asyncio
async def test_get_vehicle_by_id_not_found(httpx_mock):
    vehicle_id = 999
    url = f"{ENDPOINT_API_URL}/{vehicle_id}/"
    httpx_mock.add_response(url=url, status_code=404)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_vehicle_by_id(vehicle_id)
    assert exc_info.value.response.status_code == 404


@pytest.mark.asyncio
async def test_get_vehicle_by_id_server_error(httpx_mock):
    vehicle_id = 1
    url = f"{ENDPOINT_API_URL}/{vehicle_id}/"
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_vehicle_by_id(vehicle_id)
    assert exc_info.value.response.status_code == 500
