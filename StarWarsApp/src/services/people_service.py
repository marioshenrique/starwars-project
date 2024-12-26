from config import API_BASE_URL
from utils.url_helpers import (
    get_ids_from_urls,
)
from utils.constants import SELECTED_DATA_VEHICLE, SELECTED_DATA_PERSON
from services.external.swapi_service import get_correlated_data, get_data_list, get_data
from schemas.swapi_schemas import (
    PersonExternalSchema,
    PeopleExternalSchema,
    VehicleExternalSchema,
)

ENDPOINT_API_URL = f"{API_BASE_URL}/people"


async def get_peoples():
    url = ENDPOINT_API_URL + "/"
    data = {"people": []}
    next = url
    while next is not None:
        next, count, peoples = await get_data_list(next, PeopleExternalSchema)
        data["count"] = count
        for p in peoples:
            person_data = {key: p[key] for key in SELECTED_DATA_PERSON if key in p}
            ids_dict = await get_ids_from_urls(type_object="person", data_object=p)
            person_data.update(ids_dict)
            data["people"].append(person_data)
    return data


async def get_people_by_id(people_id: int):
    url = f"{ENDPOINT_API_URL}/{people_id}/"
    person_data = await get_data(url, PersonExternalSchema)
    data = {key: person_data[key] for key in SELECTED_DATA_PERSON if key in person_data}
    ids_dict = await get_ids_from_urls(type_object="person", data_object=person_data)
    data.update(ids_dict)
    return data


async def get_vehicles_by_people(people_id: int):
    url = f"{ENDPOINT_API_URL}/{people_id}/"
    data_correlated = await get_correlated_data(
        url=url,
        data_label="vehicles",
        main_model=PersonExternalSchema,
        related_model=VehicleExternalSchema,
    )
    data = {}
    data["people_id"] = people_id
    data["count"] = data_correlated["count"]
    data["vehicles"] = []
    for vehicle in data_correlated["vehicles"]:
        data_vehicle = {
            key: vehicle[key] for key in SELECTED_DATA_VEHICLE if key in vehicle
        }
        ids_dict = await get_ids_from_urls(type_object="vehicle", data_object=vehicle)
        data_vehicle.update(ids_dict)
        data["vehicles"].append(data_vehicle)
    return data
