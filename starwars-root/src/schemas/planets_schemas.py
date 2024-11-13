from pydantic import BaseModel, Field
from typing import List, Optional


class Planet(BaseModel):
    name: Optional[str]
    rotation_period: Optional[str]
    orbital_period: Optional[str]
    diameter: Optional[str]
    climate: Optional[str]
    gravity: Optional[str]
    terrain: Optional[str]
    surface_water: Optional[str]
    population: Optional[str]
    residents: Optional[List[str]]
    films: Optional[List[str]]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[str]


class PlanetListResponse(BaseModel):
    count: int
    planets: List[Planet]


class PlanetIDModel(BaseModel):
    planet_id: int = Field(..., ge=1)


class Residents(BaseModel):
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


class ResidentsPlanet(BaseModel):
    count: int
    residents: List[Residents]
