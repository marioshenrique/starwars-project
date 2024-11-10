from fastapi import APIRouter, HTTPException, Depends
from ..serializers.planets_serializer import PlanetListResponse, Planet, PlanetIDModel
from ..services.planets_service import get_planets, get_planet_by_id
from ..serializers.user_serializer import SafeUser
from ..dependencies.user_dependencies import get_client_user

router = APIRouter(prefix="/planets", tags=["planets"])


@router.get("/", response_model=PlanetListResponse)
async def list_planets(client: SafeUser = Depends(get_client_user)):
    return await get_planets()


@router.get("/{planet_id}/", response_model=Planet)
async def get_planet(
    planet: PlanetIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_planet_by_id(planet.planet_id)
