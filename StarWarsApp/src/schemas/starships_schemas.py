from pydantic import BaseModel, Field
from typing import List
from schemas.people_schemas import Person


class Starship(BaseModel):
    starship_id: str
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
    pilots_ids: List[str]
    films_ids: List[str]
    created: str
    edited: str

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
    starship_id: str
    count: int
    pilots: List[Person]

    class Config:
        extra = "forbid"
