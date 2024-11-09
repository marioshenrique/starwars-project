import httpx

from ..config import API_BASE_URL
from .service import get_data_list, get_data


async def get_vehicles():
    url = API_BASE_URL + "vehicles/"
    data = {"vehicles": []}
    next = url
    while next is not None:
        next, count, vehicles = await get_data_list(next)
        data["count"] = count
        for v in vehicles:
            data["vehicles"].append(v)
    return data


async def get_vehicle_by_id(vehicle_id: int):
    url = f"{API_BASE_URL}vehicles/{vehicle_id}/"
    vehicle_data = await get_data(url)
    return vehicle_data
