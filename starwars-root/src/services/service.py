import httpx
from fastapi import HTTPException, status

async def get_data_list(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data_dict = response.json()
        return data_dict["next"], data_dict["count"], data_dict["results"]
    
async def get_data(url:str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()