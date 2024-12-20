import pytest
from httpx import HTTPStatusError
from services.species_service import get_species, get_specie_by_id
from tests.species_tests.fixtures import mock_specie_data, mock_species_data
from config import API_BASE_URL

ENDPOINT_API_URL = f"{API_BASE_URL}/species"


@pytest.mark.asyncio
async def test_get_species_success(httpx_mock, mock_species_data):
    url = ENDPOINT_API_URL + "/"
    httpx_mock.add_response(url=url, json=mock_species_data, status_code=200)

    result = await get_species()
    assert result["count"] == 2
    assert len(result["species"]) == 2
    assert result["species"][0]["name"] == "Human"
    assert result["species"][1]["name"] == "Droid"


@pytest.mark.asyncio
async def test_get_species_server_error(httpx_mock):
    url = ENDPOINT_API_URL + "/"
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_species()
    assert exc_info.value.response.status_code == 500


@pytest.mark.asyncio
async def test_get_specie_by_id_success(httpx_mock, mock_specie_data):
    specie_id = 1
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    httpx_mock.add_response(url=url, json=mock_specie_data, status_code=200)

    result = await get_specie_by_id(specie_id)
    assert result["name"] == "Human"
    assert result["classification"] == "mammal"


@pytest.mark.asyncio
async def test_get_specie_by_id_not_found(httpx_mock):
    specie_id = 9999
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    httpx_mock.add_response(url=url, status_code=404)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_specie_by_id(specie_id)
    assert exc_info.value.response.status_code == 404


@pytest.mark.asyncio
async def test_get_specie_by_id_server_error(httpx_mock):
    specie_id = 1
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_specie_by_id(specie_id)
    assert exc_info.value.response.status_code == 500
