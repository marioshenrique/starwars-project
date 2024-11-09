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
