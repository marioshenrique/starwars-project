from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.films_schemas import Film
from schemas.people_schemas import Person


class Specie(BaseModel):
    name: str
    classification: str
    designation: str
    average_height: str
    skin_colors: str
    hair_colors: str
    eye_colors: str
    average_lifespan: str
    homeworld: Optional[str]
    language: str
    people: List[str]
    films: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class SpeciesListResponse(BaseModel):
    count: int
    species: List[Specie]

    class Config:
        extra = "forbid"


class SpecieIDModel(BaseModel):
    specie_id: int = Field(..., ge=1)

    class Config:
        extra = "forbid"


class FilmsSpecie(BaseModel):
    count: int
    films: List[Film]

    class Config:
        extra = "forbid"


class PeopleSpecie(BaseModel):
    count: int
    people: List[Person]

    class Config:
        extra = "forbid"
