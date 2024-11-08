import httpx

from src.config import API_BASE_URL
from .service import get_data_list, get_data

async def get_films():
    url = API_BASE_URL+"films/"
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