from fastapi import APIRouter, HTTPException, Depends
from schemas.people_schemas import (
    PeopleListResponse,
    Person,
    PeopleIDModel,
    VehiclesPeople,
)
from services.people_service import (
    get_peoples,
    get_people_by_id,
    get_vehicles_by_people,
)
from schemas.user_schemas import SafeUser
from dependencies.user_dependencies import get_client_user

router = APIRouter(prefix="/people", tags=["people"])


@router.get("", response_model=PeopleListResponse)
async def list_people(client: SafeUser = Depends(get_client_user)):
    return await get_peoples()


@router.get("/{people_id}", response_model=Person)
async def get_people(
    people: PeopleIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_people_by_id(people.people_id)


@router.get("/{people_id}/vehicles", response_model=VehiclesPeople)
async def get_vehicles(
    people: PeopleIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_vehicles_by_people(people.people_id)
