from config import API_BASE_URL
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
            data["species"].append(s)
    return data


async def get_specie_by_id(specie_id: int):
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    return await get_data(url, SpecieExternalSchema)


async def get_films_by_specie(specie_id: int):
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    data = await get_correlated_data(
        url=url,
        data_label="films",
        main_model=SpecieExternalSchema,
        related_model=FilmExternalSchema,
    )
    return data


async def get_people_by_specie(specie_id: int):
    url = f"{ENDPOINT_API_URL}/{specie_id}/"
    data = await get_correlated_data(
        url=url,
        data_label="people",
        main_model=SpecieExternalSchema,
        related_model=PersonExternalSchema,
    )
    return data
