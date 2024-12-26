from config import API_BASE_URL
from utils.url_helpers import (
    get_ids_from_urls,
)
from utils.constants import SELECTED_DATA_FILM, SELECTED_DATA_PERSON
from services.external.swapi_service import get_correlated_data, get_data_list, get_data
from schemas.swapi_schemas import (
    FilmExternalSchema,
    FilmsExternalSchema,
    PersonExternalSchema,
)

ENDPOINT_API_URL = f"{API_BASE_URL}/films"


async def get_films():
    url = ENDPOINT_API_URL + "/"
    data = {"films": []}
    next = url
    while next is not None:
        next, count, films = await get_data_list(next, FilmsExternalSchema)
        data["count"] = count
        for film in films:
            film_data = {key: film[key] for key in SELECTED_DATA_FILM if key in film}
            ids_dict = await get_ids_from_urls(type_object="film", data_object=film)
            film_data.update(ids_dict)
            data["films"].append(film_data)
    return data


async def get_film_by_id(film_id: int):
    url = f"{ENDPOINT_API_URL}/{film_id}/"
    film_data = await get_data(url, FilmExternalSchema)
    data = {key: film_data[key] for key in SELECTED_DATA_FILM if key in film_data}
    ids_dict = await get_ids_from_urls(type_object="film", data_object=film_data)
    data.update(ids_dict)
    return data


async def get_characters_by_film(film_id: int):
    url = f"{ENDPOINT_API_URL}/{film_id}/"
    data_correlated = await get_correlated_data(
        url=url,
        data_label="characters",
        main_model=FilmExternalSchema,
        related_model=PersonExternalSchema,
    )
    data = {}
    data["film_id"] = film_id
    data["count"] = data_correlated["count"]
    data["characters"] = []
    for character in data_correlated["characters"]:
        data_character = {
            key: character[key] for key in SELECTED_DATA_PERSON if key in character
        }
        ids_dict = await get_ids_from_urls(type_object="person", data_object=character)
        data_character.update(ids_dict)
        data["characters"].append(data_character)
    return data
