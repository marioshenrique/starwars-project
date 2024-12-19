import asyncio
import httpx
from pydantic import BaseModel


async def get_data(url: str, input_model: BaseModel):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        validated_data = input_model.parse_obj(data)
        return validated_data.dict()


async def get_data_list(url: str, input_model: BaseModel):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        validated_data = input_model.parse_obj(data)
        validated_data_dict = validated_data.dict()
        return (
            validated_data_dict["next"],
            validated_data_dict["count"],
            validated_data_dict["results"],
        )


async def get_correlated_data(
    url: str, data_label: str, main_model: BaseModel, related_model: BaseModel
):
    data = {}
    object_data = await get_data(url, main_model)
    data["count"] = int(len(object_data[data_label]))
    data[data_label] = []
    tasks = [get_data(item_url, related_model) for item_url in object_data[data_label]]
    results = await asyncio.gather(*tasks)
    data[data_label] = results
    return data
