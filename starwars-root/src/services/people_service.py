import httpx

from ..config import API_BASE_URL
from .service import get_data_list, get_data


async def get_peoples():
    url = API_BASE_URL + "people/"
    data = {"peoples": []}
    next = url
    while next is not None:
        next, count, peoples = await get_data_list(next)
        data["count"] = count
        for p in peoples:
            data["peoples"].append(p)
    return data


async def get_people_by_id(people_id: int):
    url = f"{API_BASE_URL}people/{people_id}/"
    return await get_data(url)
