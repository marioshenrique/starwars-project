from pydantic import BaseModel, Field
from typing import List, Optional


class Person(BaseModel):
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


class PeopleListResponse(BaseModel):
    count: int
    peoples: List[Person]


class PeopleIDModel(BaseModel):
    people_id: int = Field(..., ge=1)


class Vehicle(BaseModel):
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


class VehiclesPeople(BaseModel):
    count: int
    vehicles: List[Vehicle]
