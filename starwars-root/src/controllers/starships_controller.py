from fastapi import APIRouter, HTTPException, Depends
from ..schemas.starships_schemas import (
    StarshipsListResponse,
    Starship,
    StarshipIDModel,
)
from ..services.starships_service import get_starships, get_starship_by_id
from ..schemas.user_schemas import SafeUser
from ..dependencies.user_dependencies import get_client_user

router = APIRouter(prefix="/starships", tags=["starships"])


@router.get("", response_model=StarshipsListResponse)
async def list_starships(client: SafeUser = Depends(get_client_user)):
    return await get_starships()


@router.get("/{starship_id}", response_model=Starship)
async def get_starship(
    starship: StarshipIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_starship_by_id(starship.starship_id)
