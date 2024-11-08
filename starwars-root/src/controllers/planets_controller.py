from fastapi import APIRouter, HTTPException, Depends
from src.models.planets_model import PlanetListResponse, Planet, PlanetIDModel
from src.services.planets_service import get_planets, get_planet_by_id

router = APIRouter(
    prefix="/planets",
    tags=["planets"]
)

@router.get("/", response_model=PlanetListResponse)
async def list_planets():
    return await get_planets() 

@router.get("/{planet_id}/", response_model=Planet)
async def get_planet(planet: PlanetIDModel = Depends()):
    return await get_planet_by_id(planet.planet_id)