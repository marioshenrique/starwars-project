import httpx

from config import API_BASE_URL
from services.external.swapi_service import get_correlated_data, get_data_list, get_data

ENDPOINT_API_URL = f"{API_BASE_URL}/planets"


async def get_planets():
    url = ENDPOINT_API_URL
    data = {"planets": []}
    next = url
    while next is not None:
        next, count, planets = await get_data_list(next)
        data["count"] = count
        for p in planets:
            data["planets"].append(p)
    return data


async def get_planet_by_id(planet_id: int):
    url = f"{ENDPOINT_API_URL}/{planet_id}/"
    return await get_data(url)


async def get_residents_by_planet(planet_id: int):
    url = f"{ENDPOINT_API_URL}/{planet_id}/"
    data = await get_correlated_data(url=url, data_label="residents")
    return data
