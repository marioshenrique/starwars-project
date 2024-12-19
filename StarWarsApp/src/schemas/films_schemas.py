from pydantic import BaseModel, Field
from typing import List
from schemas.people_schemas import Person


class Film(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    characters: List[str]
    planets: List[str]
    starships: List[str]
    vehicles: List[str]
    species: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class FilmList(BaseModel):
    count: int
    films: List[Film]

    class Config:
        extra = "forbid"


class FilmIDModel(BaseModel):
    film_id: int = Field(..., ge=1)

    class Config:
        extra = "forbid"


class CharactersFilm(BaseModel):
    count: int
    characters: List[Person]

    class Config:
        extra = "forbid"
