import asyncio
import httpx


async def get_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()


async def get_data_list(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data_dict = response.json()
        return data_dict["next"], data_dict["count"], data_dict["results"]


async def get_correlated_data(url: str, data_label: str):
    data = {}
    object_data = await get_data(url)
    data["count"] = int(len(object_data[data_label]))
    data[data_label] = []
    tasks = [get_data(item_url) for item_url in object_data[data_label]]
    results = await asyncio.gather(*tasks)
    data[data_label] = results
    return data
