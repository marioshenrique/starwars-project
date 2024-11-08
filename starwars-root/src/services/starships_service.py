import httpx

from src.config import API_BASE_URL
from .service import get_data_list, get_data

async def get_starships():
    url = API_BASE_URL+"starships/"
    data = {"starships": []}
    next = url
    while next is not None:
        next, count, starships = await get_data_list(next)
        data["count"] = count
        for s in starships:
            data["starships"].append(s)
    return data

async def get_starship_by_id(starship_id: int):
    url = f"{API_BASE_URL}starships/{starship_id}/"
    return await get_data(url)