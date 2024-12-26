from pydantic import BaseModel, Field
from typing import List
from schemas.people_schemas import Person


class Film(BaseModel):
    film_id: str
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    created: str
    edited: str
    characters_ids: List[str]
    planets_ids: List[str]
    starships_ids: List[str]
    vehicles_ids: List[str]
    species_ids: List[str]

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
    film_id: str
    count: int
    characters: List[Person]

    class Config:
        extra = "forbid"
