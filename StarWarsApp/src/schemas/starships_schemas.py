from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.people_schemas import Person


class Starship(BaseModel):
    name: Optional[str]
    model: Optional[str]
    manufacturer: Optional[str]
    cost_in_credits: Optional[str]
    length: Optional[str]
    max_atmosphering_speed: Optional[str]
    crew: Optional[str]
    passengers: Optional[str]
    cargo_capacity: Optional[str]
    consumables: Optional[str]
    hyperdrive_rating: Optional[str]
    MGLT: Optional[str]
    starship_class: Optional[str]
    pilots: Optional[List[str]]
    films: Optional[List[str]]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[str]


class StarshipsListResponse(BaseModel):
    count: int
    starships: List[Starship]


class StarshipIDModel(BaseModel):
    starship_id: int = Field(..., ge=1)


class PilotsStarship(BaseModel):
    count: int
    pilots: List[Person]
