from fastapi import APIRouter, HTTPException, Depends
from src.models.people_model import PeopleListResponse, Person, PeopleIDModel
from src.services.people_service import get_peoples, get_people_by_id

router = APIRouter(
    prefix="/people",
    tags=["people"]
)

@router.get("/", response_model=PeopleListResponse)
async def list_people():
    return await get_peoples() 

@router.get("/{people_id}/", response_model=Person)
async def get_people(people: PeopleIDModel = Depends()):
    return await get_people_by_id(people.people_id)