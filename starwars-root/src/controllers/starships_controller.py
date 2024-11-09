from fastapi import APIRouter, HTTPException, Depends
from src.models.starships_model import StarshipsListResponse, Starship, StarshipIDModel
from src.services.starships_service import get_starships, get_starship_by_id

router = APIRouter(prefix="/starships", tags=["starships"])


@router.get("/", response_model=StarshipsListResponse)
async def list_starships():
    return await get_starships()


@router.get("/{starship_id}/", response_model=Starship)
async def get_starship(starship: StarshipIDModel = Depends()):
    return await get_starship_by_id(starship.starship_id)
