from pydantic import BaseModel, Field
from typing import List
from schemas.people_schemas import Person


class Planet(BaseModel):
    name: str
    rotation_period: str
    orbital_period: str
    diameter: str
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: List[str]
    films: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class PlanetListResponse(BaseModel):
    count: int
    planets: List[Planet]

    class Config:
        extra = "forbid"


class PlanetIDModel(BaseModel):
    planet_id: int = Field(..., ge=1)

    class Config:
        extra = "forbid"


class ResidentsPlanet(BaseModel):
    count: int
    residents: List[Person]

    class Config:
        extra = "forbid"
