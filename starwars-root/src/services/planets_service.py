import httpx

from src.config import API_BASE_URL
from .service import get_data_list, get_data

async def get_planets():
    url = API_BASE_URL+"planets/"
    data = {"planets": []}
    next = url
    while next is not None:
        next, count, planets = await get_data_list(next)
        data["count"] = count
        for p in planets:
            data["planets"].append(p)
    return data

async def get_planet_by_id(planet_id: int):
    url = f"{API_BASE_URL}planets/{planet_id}/"
    return await get_data(url)