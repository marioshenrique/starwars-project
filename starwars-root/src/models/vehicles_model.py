from pydantic import BaseModel, Field
from typing import List, Optional

class Vehicles(BaseModel):
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
    vehicle_class: Optional[str]
    pilots: Optional[List[str]]
    films: Optional[List[str]]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[str]

class VehiclesListResponse(BaseModel):
    count: int
    vehicles: List[Vehicles]

class VehiclesIDModel(BaseModel):
    vehicle_id: int = Field(..., ge=1)