from config import API_BASE_URL
from utils.url_helpers import get_ids_from_urls
from utils.constants import SELECTED_DATA_STARSHIP, SELECTED_DATA_PERSON
from services.external.swapi_service import get_correlated_data, get_data_list, get_data
from schemas.swapi_schemas import (
    StarshipExternalSchema,
    StarshipsExternalSchema,
    PersonExternalSchema,
)

ENDPOINT_API_URL = f"{API_BASE_URL}/starships"


async def get_starships():
    url = ENDPOINT_API_URL + "/"
    data = {"starships": []}
    next = url
    while next is not None:
        next, count, starships = await get_data_list(next, StarshipsExternalSchema)
        data["count"] = count
        for s in starships:
            starship_data = {key: s[key] for key in SELECTED_DATA_STARSHIP if key in s}
            ids_dict = await get_ids_from_urls(type_object="starship", data_object=s)
            starship_data.update(ids_dict)
            data["starships"].append(starship_data)
    return data


async def get_starship_by_id(starship_id: int):
    url = f"{ENDPOINT_API_URL}/{starship_id}/"
    starship_data = await get_data(url, StarshipExternalSchema)
    data = {
        key: starship_data[key]
        for key in SELECTED_DATA_STARSHIP
        if key in starship_data
    }
    ids_dict = await get_ids_from_urls(
        type_object="starship", data_object=starship_data
    )
    data.update(ids_dict)
    return data


async def get_pilots_by_starship(starship_id: int):
    url = f"{ENDPOINT_API_URL}/{starship_id}/"
    data_correlated = await get_correlated_data(
        url=url,
        data_label="pilots",
        main_model=StarshipExternalSchema,
        related_model=PersonExternalSchema,
    )
    data = {}
    data["starship_id"] = starship_id
    data["count"] = data_correlated["count"]
    data["pilots"] = []
    for pilot in data_correlated["pilots"]:
        data_pilot = {key: pilot[key] for key in SELECTED_DATA_PERSON if key in pilot}
        ids_dict = await get_ids_from_urls(type_object="person", data_object=pilot)
        data_pilot.update(ids_dict)
        data["pilots"].append(data_pilot)
    return data
