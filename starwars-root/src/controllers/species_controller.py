from fastapi import APIRouter, HTTPException, Depends
from schemas.species_schemas import (
    SpeciesListResponse,
    Specie,
    SpecieIDModel,
    FilmsSpecie,
    PeopleSpecie,
)
from services.species_service import (
    get_species,
    get_specie_by_id,
    get_films_by_specie,
    get_people_by_specie,
)

router = APIRouter(prefix="/species", tags=["species"])


@router.get("", response_model=SpeciesListResponse)
async def list_species():
    return await get_species()


@router.get("/{specie_id}", response_model=Specie)
async def get_specie(
    specie: SpecieIDModel = Depends()):
    return await get_specie_by_id(specie.specie_id)


@router.get("/{specie_id}/people", response_model=PeopleSpecie)
async def get_people(
    specie: SpecieIDModel = Depends()):
    return await get_people_by_specie(specie.specie_id)


@router.get("/{specie_id}/films", response_model=FilmsSpecie)
async def get_films(
    specie: SpecieIDModel = Depends()):
    return await get_films_by_specie(specie.specie_id)
