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


class Character(BaseModel):
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


class CharactersFilm(BaseModel):
    count: int
    characters: List[Character]
