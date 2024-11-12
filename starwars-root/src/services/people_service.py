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


async def get_vehicles_by_people(people_id: int):
    url = f"{API_BASE_URL}people/{people_id}/"
    data = {}
    people_data = await get_data(url)
    data["count"] = int(len(people_data["vehicles"]))
    data["vehicles"] = []
    for c in people_data["vehicles"]:
        url = c
        vehicle_data = await get_data(url)
        data["vehicles"].append(vehicle_data)
    return data
