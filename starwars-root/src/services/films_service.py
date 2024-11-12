import httpx

from ..config import API_BASE_URL
from .service import get_data_list, get_data


async def get_films():
    url = API_BASE_URL + "films/"
    data = {"films": []}
    next = url
    while next is not None:
        next, count, films = await get_data_list(next)
        data["count"] = count
        for film in films:
            data["films"].append(film)
    return data


async def get_film_by_id(film_id: int):
    url = f"{API_BASE_URL}films/{film_id}/"
    return await get_data(url)


async def get_characters_by_film(film_id: int):
    url = f"{API_BASE_URL}films/{film_id}/"
    data = {}
    film_data = await get_data(url)
    data["count"] = int(len(film_data["characters"]))
    data["characters"] = []
    for c in film_data["characters"]:
        url = c
        character_data = await get_data(url)
        data["characters"].append(character_data)
    return data
