from pydantic import BaseModel, Field
from typing import List


class Vehicle(BaseModel):
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
    vehicle_class: str
    pilots: List[str]
    films: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class VehiclesListResponse(BaseModel):
    count: int
    vehicles: List[Vehicle]

    class Config:
        extra = "forbid"


class VehicleIDModel(BaseModel):
    vehicle_id: int = Field(..., ge=1)

    class Config:
        extra = "forbid"
