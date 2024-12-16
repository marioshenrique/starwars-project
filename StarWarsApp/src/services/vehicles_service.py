from config import API_BASE_URL
from services.external.swapi_service import get_correlated_data, get_data_list, get_data

ENDPOINT_API_URL = f"{API_BASE_URL}/vehicles"


async def get_vehicles():
    url = ENDPOINT_API_URL + "/"
    data = {"vehicles": []}
    next = url
    while next is not None:
        next, count, vehicles = await get_data_list(next)
        data["count"] = count
        for v in vehicles:
            data["vehicles"].append(v)
    return data


async def get_vehicle_by_id(vehicle_id: int):
    url = f"{ENDPOINT_API_URL}/{vehicle_id}/"
    vehicle_data = await get_data(url)
    return vehicle_data
