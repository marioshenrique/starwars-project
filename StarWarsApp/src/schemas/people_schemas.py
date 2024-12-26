from pydantic import BaseModel, Field
from typing import List
from schemas.vehicles_schemas import Vehicle


class Person(BaseModel):
    person_id: str
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    home_planet_id: str
    films_ids: List[str]
    species_ids: List[str]
    vehicles_ids: List[str]
    starships_ids: List[str]
    created: str
    edited: str

    class Config:
        extra = "forbid"


class PeopleListResponse(BaseModel):
    count: int
    people: List[Person]

    class Config:
        extra = "forbid"


class PeopleIDModel(BaseModel):
    people_id: int = Field(..., ge=1)

    class Config:
        extra = "forbid"


class VehiclesPeople(BaseModel):
    people_id: str
    count: int
    vehicles: List[Vehicle]

    class Config:
        extra = "forbid"
