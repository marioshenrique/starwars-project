import pytest
from httpx import HTTPStatusError
from src.services.planets_service import get_planet_by_id, get_planets
from .fixtures import mock_planet_data, mock_planets_data
from src.config import API_BASE_URL

ENDPOINT_API_URL = f"{API_BASE_URL}/planets"


@pytest.mark.asyncio
async def test_get_planets_success(httpx_mock, mock_planets_data):
    url = ENDPOINT_API_URL
    httpx_mock.add_response(url=url, json=mock_planets_data, status_code=200)

    result = await get_planets()
    assert result["count"] == 2
    assert result["planets"][0]["name"] == "Tatooine"
    assert result["planets"][1]["name"] == "Alderaan"
    assert len(result["planets"]) == 2


@pytest.mark.asyncio
async def test_get_planets_server_error(httpx_mock):
    url = ENDPOINT_API_URL
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_planets()
    assert exc_info.value.response.status_code == 500


@pytest.mark.asyncio
async def test_get_planet_by_id_success(httpx_mock, mock_planet_data):
    planet_id = 6
    url = f"{ENDPOINT_API_URL}/{planet_id}/"
    httpx_mock.add_response(url=url, json=mock_planet_data, status_code=200)

    result = await get_planet_by_id(planet_id)
    assert result["name"] == "Bespin"
    assert result["rotation_period"] == "12"
    assert result["orbital_period"] == "5110"


@pytest.mark.asyncio
async def test_get_planet_by_id_not_found(httpx_mock):
    planet_id = 999
    url = f"{ENDPOINT_API_URL}/{planet_id}/"
    httpx_mock.add_response(url=url, status_code=404)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_planet_by_id(planet_id)
    assert exc_info.value.response.status_code == 404


@pytest.mark.asyncio
async def test_get_planet_by_id_server_error(httpx_mock):
    planet_id = 1
    url = f"{ENDPOINT_API_URL}/{planet_id}/"
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_planet_by_id(planet_id)
    assert exc_info.value.response.status_code == 500
