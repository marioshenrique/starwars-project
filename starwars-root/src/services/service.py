from ..config import API_BASE_URL
from ..repository.repository import get_data


async def get_correlated_data(url: str, data_label: str):
    data = {}
    object_data = await get_data(url)
    data["count"] = int(len(object_data[data_label]))
    data[data_label] = []
    for i in object_data[data_label]:
        url = i
        item_data = await get_data(url)
        data[data_label].append(item_data)
    return data
