import httpx

from src.config import API_BASE_URL
from .service import get_data_list, get_data


async def get_species():
    url = API_BASE_URL + "species/"
    data = {"species": []}
    next = url
    while next is not None:
        next, count, species = await get_data_list(next)
        data["count"] = count
        for s in species:
            data["species"].append(s)
    return data


async def get_specie_by_id(specie_id: int):
    url = f"{API_BASE_URL}species/{specie_id}/"
    return await get_data(url)
