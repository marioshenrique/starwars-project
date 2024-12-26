from config import API_BASE_URL
from utils.url_helpers import get_ids_from_urls
from utils.constants import (
    SELECTED_DATA_FILM,
    SELECTED_DATA_PERSON,
    SELECTED_DATA_SPECIE,
)
from services.external.swapi_service import get_correlated_data, get_data_list, get_data
from schemas.swapi_schemas import (
    SpecieExternalSchema,
    SpeciesExternalSchema,
    FilmExternalSchema,
    PersonExternalSchema,
)

ENDPOINT_API_URL = f"{API_BASE_URL}/species"


async def get_species():
    url = ENDPOINT_API_URL + "/"
    data = {"species": []}
    next = url
    while next is not None:
        next, count, species = await get_data_list(next, SpeciesExternalSchema)
        data["count"] = count
        for s in species:
            specie_data = {key: s[key] for key in SELECTED_DATA_SPECIE if key in s}
            ids_dict = await get_ids_from_urls(type_object="specie", data_object=s)
            specie_data.update(ids_dict)
            data["species"].append(specie_data)
    return data


async def get_specie_by_id(specie_id: int):
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    specie_data = await get_data(url, SpecieExternalSchema)
    data = {key: specie_data[key] for key in SELECTED_DATA_SPECIE if key in specie_data}
    ids_dict = await get_ids_from_urls(type_object="specie", data_object=specie_data)
    data.update(ids_dict)
    return data


async def get_films_by_specie(specie_id: int):
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    data_correlated = await get_correlated_data(
        url=url,
        data_label="films",
        main_model=SpecieExternalSchema,
        related_model=FilmExternalSchema,
    )
    data = {}
    data["specie_id"] = specie_id
    data["count"] = data_correlated["count"]
    data["films"] = []
    for film in data_correlated["films"]:
        data_film = {key: film[key] for key in SELECTED_DATA_FILM if key in film}
        ids_dict = await get_ids_from_urls(type_object="film", data_object=film)
        data_film.update(ids_dict)
        data["films"].append(data_film)
    return data


async def get_people_by_specie(specie_id: int):
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    data_correlated = await get_correlated_data(
        url=url,
        data_label="people",
        main_model=SpecieExternalSchema,
        related_model=PersonExternalSchema,
    )
    data = {}
    data["specie_id"] = specie_id
    data["count"] = data_correlated["count"]
    data["people"] = []
    for person in data_correlated["people"]:
        data_person = {
            key: person[key] for key in SELECTED_DATA_PERSON if key in person
        }
        ids_dict = await get_ids_from_urls(type_object="person", data_object=person)
        data_person.update(ids_dict)
        data["people"].append(data_person)
    return data
