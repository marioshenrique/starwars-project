from pydantic import BaseModel, Field
from typing import List
from schemas.people_schemas import Person


class Starship(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    pilots: List[str]
    films: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class StarshipsListResponse(BaseModel):
    count: int
    starships: List[Starship]

    class Config:
        extra = "forbid"


class StarshipIDModel(BaseModel):
    starship_id: int = Field(..., ge=1)

    class Config:
        extra = "forbid"


class PilotsStarship(BaseModel):
    count: int
    pilots: List[Person]

    class Config:
        extra = "forbid"
