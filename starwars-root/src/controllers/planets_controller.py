from fastapi import APIRouter, HTTPException, Depends
from schemas.planets_schemas import (
    PlanetListResponse,
    Planet,
    PlanetIDModel,
    ResidentsPlanet,
)
from services.planets_service import (
    get_planets,
    get_planet_by_id,
    get_residents_by_planet,
)

router = APIRouter(prefix="/planets", tags=["planets"])


@router.get("", response_model=PlanetListResponse)
async def list_planets():
    return await get_planets()


@router.get("/{planet_id}", response_model=Planet)
async def get_planet(planet: PlanetIDModel = Depends()):
    return await get_planet_by_id(planet.planet_id)


@router.get("/{planet_id}/residents", response_model=ResidentsPlanet)
async def get_residents(planet: PlanetIDModel = Depends()):
    return await get_residents_by_planet(planet.planet_id)
