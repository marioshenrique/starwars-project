import asyncio
from ..config import API_BASE_URL
from ..repository.repository import get_data


async def get_correlated_data(url: str, data_label: str):
    data = {}
    object_data = await get_data(url)
    data["count"] = int(len(object_data[data_label]))
    data[data_label] = []
    tasks = [get_data(item_url) for item_url in object_data[data_label]]
    results = await asyncio.gather(*tasks)
    data[data_label] = results
    return data
