import httpx

from ..config import API_BASE_URL
from ..repository.repository import get_data_list, get_data
from .service import get_correlated_data

ENDPOINT_API_URL = f"{API_BASE_URL}/starships"


async def get_starships():
    url = ENDPOINT_API_URL
    data = {"starships": []}
    next = url
    while next is not None:
        next, count, starships = await get_data_list(next)
        data["count"] = count
        for s in starships:
            data["starships"].append(s)
    return data


async def get_starship_by_id(starship_id: int):
    url = f"{ENDPOINT_API_URL}/{starship_id}/"
    return await get_data(url)


async def get_pilots_by_starship(starship_id: int):
    url = f"{ENDPOINT_API_URL}/{starship_id}/"
    data = await get_correlated_data(url=url, data_label="pilots")
    return data
