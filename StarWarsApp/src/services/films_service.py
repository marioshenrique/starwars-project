from config import API_BASE_URL
from services.external.swapi_service import get_correlated_data, get_data_list, get_data
from schemas.swapi_schemas import FilmExternalSchema, FilmsExternalSchema, PersonExternalSchema

ENDPOINT_API_URL = f"{API_BASE_URL}/films"


async def get_films():
    url = ENDPOINT_API_URL + "/"
    data = {"films": []}
    next = url
    while next is not None:
        next, count, films = await get_data_list(next, FilmsExternalSchema)
        data["count"] = count
        for film in films:
            data["films"].append(film)
    return data


async def get_film_by_id(film_id: int):
    url = f"{ENDPOINT_API_URL}/{film_id}/"
    return await get_data(url, FilmExternalSchema)


async def get_characters_by_film(film_id: int):
    url = f"{ENDPOINT_API_URL}/{film_id}/"
    data = await get_correlated_data(url=url, data_label="characters", main_model=FilmExternalSchema, related_model=PersonExternalSchema)
    return data
