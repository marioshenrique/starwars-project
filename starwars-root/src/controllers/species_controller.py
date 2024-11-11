from fastapi import APIRouter, HTTPException, Depends
from ..serializers.species_serializer import SpeciesListResponse, Specie, SpecieIDModel
from ..services.species_service import get_species, get_specie_by_id
from ..serializers.user_serializer import SafeUser
from ..dependencies.user_dependencies import get_client_user

router = APIRouter(prefix="/species", tags=["species"])


@router.get("", response_model=SpeciesListResponse)
async def list_species(client: SafeUser = Depends(get_client_user)):
    return await get_species()


@router.get("/{specie_id}", response_model=Specie)
async def get_specie(
    specie: SpecieIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_specie_by_id(specie.specie_id)
