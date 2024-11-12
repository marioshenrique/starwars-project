from pydantic import BaseModel, Field
from typing import List, Optional


class Film(BaseModel):
    title: Optional[str]
    episode_id: Optional[int]
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


class FilmList(BaseModel):
    count: int
    films: List[Film]


class FilmIDModel(BaseModel):
    film_id: int = Field(..., ge=1)
