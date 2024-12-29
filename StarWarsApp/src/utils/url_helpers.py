import asyncio
from urllib.parse import urlparse

COLUMNS_BY_TYPE = {
    "person": ["films", "species", "vehicles", "starships"],
    "film": ["characters", "planets", "starships", "vehicles", "species"],
    "vehicle": ["pilots", "films"],
    "planet": ["residents", "films"],
    "specie": ["people", "films"],
    "starship": ["pilots", "films"],
}


async def get_objetc_ids_from_urls_async(url_list: list):
    tasks = [get_element_from_url(item_url, -1) for item_url in url_list]
    data = await asyncio.gather(*tasks)
    return data


async def get_ids_from_urls(type_object: str, data_object: dict):
    objects_ids_list = [
        await get_objetc_ids_from_urls_async(url_list=data_object[c])
        for c in COLUMNS_BY_TYPE[type_object]
    ]
    data_dict = {
        COLUMNS_BY_TYPE[type_object][i] + "_ids": objects_ids_list[i]
        for i in range(len(COLUMNS_BY_TYPE[type_object]))
    }
    data_dict[type_object + "_id"] = await get_element_from_url(
        url=data_object["url"], position=-1
    )
    if type_object == "person" or type_object == "specie":
        data_dict["home_planet_id"] = await get_element_from_url(
            url=data_object["homeworld"], position=-1
        )
    return data_dict


async def get_element_from_url(url, position: str):
    if not url or not position:
        return None
    path = urlparse(url).path
    segments = path.strip("/").split("/")
    if abs(position) < len(segments):
        return segments[position]
    return None
