import pytest
from httpx import HTTPStatusError
from src.services.films_service import get_film_by_id, get_films
from .fixtures import mock_films_data, mock_film_data
from src.config import API_BASE_URL

ENDPOINT_API_URL = f"{API_BASE_URL}/films"


@pytest.mark.asyncio
async def test_get_films_success(httpx_mock, mock_films_data):
    url = ENDPOINT_API_URL
    httpx_mock.add_response(url=url, json=mock_films_data, status_code=200)

    result = await get_films()
    assert result["count"] == 2
    assert result["films"][0]["title"] == "A New Hope"
    assert result["films"][1]["title"] == "The Empire Strikes Back"


@pytest.mark.asyncio
async def test_get_films_server_error(httpx_mock):
    url = ENDPOINT_API_URL
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_films()
    assert exc_info.value.response.status_code == 500


@pytest.mark.asyncio
async def test_get_film_by_id_success(httpx_mock, mock_film_data):
    film_id = 1
    url = f"{ENDPOINT_API_URL}/{film_id}/"
    httpx_mock.add_response(url=url, json=mock_film_data, status_code=200)

    result = await get_film_by_id(film_id)
    assert result["title"] == "A New Hope"
    assert result["episode_id"] == 4


@pytest.mark.asyncio
async def test_get_film_by_id_not_found(httpx_mock):
    film_id = 9999
    url = f"{ENDPOINT_API_URL}/{film_id}/"
    httpx_mock.add_response(url=url, status_code=404)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_film_by_id(film_id)
    assert exc_info.value.response.status_code == 404


@pytest.mark.asyncio
async def test_get_film_by_id_server_error(httpx_mock):
    film_id = 1
    url = f"{ENDPOINT_API_URL}/{film_id}/"
    httpx_mock.add_response(url=url, status_code=500)

    with pytest.raises(HTTPStatusError) as exc_info:
        await get_film_by_id(film_id)
    assert exc_info.value.response.status_code == 500
