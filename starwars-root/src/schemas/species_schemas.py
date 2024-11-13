from pydantic import BaseModel, Field
from typing import List, Optional


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


class Film(BaseModel):
    title: Optional[str]
    episode_id: Optional[str]
    opening_crawl: Optional[str]
    director: Optional[str]
    producer: Optional[str]
    release_date: Optional[str]
    characters: Optional[List[str]]
    planets: Optional[List[str]]
    starships: Optional[List[str]]
    vehicles: Optional[List[str]]
    species: Optional[List[str]]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[str]


class FilmsSpecie(BaseModel):
    count: int
    films: List[Film]


class People(BaseModel):
    name: Optional[str]
    height: Optional[str]
    mass: Optional[str]
    hair_color: Optional[str]
    skin_color: Optional[str]
    eye_color: Optional[str]
    birth_year: Optional[str]
    gender: Optional[str]
    homeworld: Optional[str]
    films: Optional[List[str]]
    species: Optional[List[str]]
    vehicles: Optional[List[str]]
    starships: Optional[List[str]]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[str]


class PeopleSpecie(BaseModel):
    count: int
    people: List[People]
