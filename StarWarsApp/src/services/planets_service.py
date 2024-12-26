from config import API_BASE_URL
from utils.url_helpers import get_ids_from_urls
from utils.constants import SELECTED_DATA_PLANET, SELECTED_DATA_PERSON
from services.external.swapi_service import get_correlated_data, get_data_list, get_data
from schemas.swapi_schemas import (
    PlanetExternalSchema,
    PlanetsExternalSchema,
    PersonExternalSchema,
)

ENDPOINT_API_URL = f"{API_BASE_URL}/planets"


async def get_planets():
    url = ENDPOINT_API_URL + "/"
    data = {"planets": []}
    next = url
    while next is not None:
        next, count, planets = await get_data_list(next, PlanetsExternalSchema)
        data["count"] = count
        for p in planets:
            planet_data = {key: p[key] for key in SELECTED_DATA_PLANET if key in p}
            ids_dict = await get_ids_from_urls(type_object="planet", data_object=p)
            planet_data.update(ids_dict)
            data["planets"].append(planet_data)
    return data


async def get_planet_by_id(planet_id: int):
    url = f"{ENDPOINT_API_URL}/{planet_id}/"
    planet_data = await get_data(url, PlanetExternalSchema)
    data = {key: planet_data[key] for key in SELECTED_DATA_PLANET if key in planet_data}
    ids_dict = await get_ids_from_urls(type_object="planet", data_object=planet_data)
    data.update(ids_dict)
    return data


async def get_residents_by_planet(planet_id: int):
    url = f"{ENDPOINT_API_URL}/{planet_id}/"
    data_correlated = await get_correlated_data(
        url=url,
        data_label="residents",
        main_model=PlanetExternalSchema,
        related_model=PersonExternalSchema,
    )
    data = {}
    data["planet_id"] = planet_id
    data["count"] = data_correlated["count"]
    data["residents"] = []
    for resident in data_correlated["residents"]:
        data_resident = {
            key: resident[key] for key in SELECTED_DATA_PERSON if key in resident
        }
        ids_dict = await get_ids_from_urls(type_object="person", data_object=resident)
        data_resident.update(ids_dict)
        data["residents"].append(data_resident)
    return data
