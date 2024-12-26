from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.films_schemas import Film
from schemas.people_schemas import Person


class Specie(BaseModel):
    specie_id: str
    name: str
    classification: str
    designation: str
    average_height: str
    skin_colors: str
    hair_colors: str
    eye_colors: str
    average_lifespan: str
    home_planet_id: Optional[str]
    language: str
    people_ids: List[str]
    films_ids: List[str]
    created: str
    edited: str

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
    specie_id: str
    count: int
    films: List[Film]

    class Config:
        extra = "forbid"


class PeopleSpecie(BaseModel):
    specie_id: str
    count: int
    people: List[Person]

    class Config:
        extra = "forbid"
