from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.films_schemas import Film
from schemas.people_schemas import Person


class Specie(BaseModel):
    name: Optional[str]
    classification: Optional[str]
    designation: Optional[str]
    average_height: Optional[str]
    skin_colors: Optional[str]
    hair_colors: Optional[str]
    eye_colors: Optional[str]
    average_lifespan: Optional[str]
    homeworld: Optional[str]
    language: Optional[str]
    people: Optional[List[str]]
    films: Optional[List[str]]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[str]


class SpeciesListResponse(BaseModel):
    count: int
    species: List[Specie]


class SpecieIDModel(BaseModel):
    specie_id: int = Field(..., ge=1)


class FilmsSpecie(BaseModel):
    count: int
    films: List[Film]


class PeopleSpecie(BaseModel):
    count: int
    people: List[Person]
