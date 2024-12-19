from pydantic import BaseModel, Field
from typing import List
from schemas.vehicles_schemas import Vehicle


class Person(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class PeopleListResponse(BaseModel):
    count: int
    peoples: List[Person]

    class Config:
        extra = "forbid"


class PeopleIDModel(BaseModel):
    people_id: int = Field(..., ge=1)

    class Config:
        extra = "forbid"


class VehiclesPeople(BaseModel):
    count: int
    vehicles: List[Vehicle]

    class Config:
        extra = "forbid"
