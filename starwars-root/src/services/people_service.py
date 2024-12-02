import httpx

from config import API_BASE_URL
from services.external.swapi_service import get_correlated_data, get_data_list, get_data

ENDPOINT_API_URL = f"{API_BASE_URL}/people"


async def get_peoples():
    url = ENDPOINT_API_URL
    data = {"peoples": []}
    next = url
    while next is not None:
        next, count, peoples = await get_data_list(next)
        data["count"] = count
        for p in peoples:
            data["peoples"].append(p)
    return data


async def get_people_by_id(people_id: int):
    url = f"{ENDPOINT_API_URL}/{people_id}/"
    return await get_data(url)


async def get_vehicles_by_people(people_id: int):
    url = f"{ENDPOINT_API_URL}/{people_id}/"
    data = await get_correlated_data(url=url, data_label="vehicles")
    return data
