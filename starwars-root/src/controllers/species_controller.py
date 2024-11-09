from fastapi import APIRouter, HTTPException, Depends
from src.models.species_model import SpeciesListResponse, Specie, SpecieIDModel
from src.services.species_service import get_species, get_specie_by_id

router = APIRouter(prefix="/species", tags=["species"])


@router.get("/", response_model=SpeciesListResponse)
async def list_species():
    return await get_species()


@router.get("/{specie_id}/", response_model=Specie)
async def get_specie(specie: SpecieIDModel = Depends()):
    return await get_specie_by_id(specie.specie_id)
