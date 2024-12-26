from config import API_BASE_URL
from utils.url_helpers import get_ids_from_urls
from utils.constants import SELECTED_DATA_VEHICLE
from services.external.swapi_service import get_data_list, get_data
from schemas.swapi_schemas import VehicleExternalSchema, VehiclesExternalSchema

ENDPOINT_API_URL = f"{API_BASE_URL}/vehicles"


async def get_vehicles():
    url = ENDPOINT_API_URL + "/"
    data = {"vehicles": []}
    next = url
    while next is not None:
        next, count, vehicles = await get_data_list(next, VehiclesExternalSchema)
        data["count"] = count
        for v in vehicles:
            vehicle_data = {key: v[key] for key in SELECTED_DATA_VEHICLE if key in v}
            ids_dict = await get_ids_from_urls(type_object="vehicle", data_object=v)
            vehicle_data.update(ids_dict)
            data["vehicles"].append(vehicle_data)
    return data


async def get_vehicle_by_id(vehicle_id: int):
    url = f"{ENDPOINT_API_URL}/{vehicle_id}/"
    vehicle_data = await get_data(url, VehicleExternalSchema)
    data = {
        key: vehicle_data[key] for key in SELECTED_DATA_VEHICLE if key in vehicle_data
    }
    ids_dict = await get_ids_from_urls(type_object="vehicle", data_object=vehicle_data)
    data.update(ids_dict)
    return data
