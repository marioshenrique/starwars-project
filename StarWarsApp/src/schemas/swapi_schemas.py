from pydantic import BaseModel
from typing import List


class MainExternalSchema(BaseModel):
    count: int
    next: str = None
    previous: str = None

    class Config:
        extra = "forbid"


class FilmExternalSchema(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    characters: List[str]
    planets: List[str]
    starships: List[str]
    vehicles: List[str]
    species: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class FilmsExternalSchema(MainExternalSchema):
    results: List[FilmExternalSchema]

    class Config:
        extra = "forbid"


class PersonExternalSchema(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class PeopleExternalSchema(MainExternalSchema):
    results: List[PersonExternalSchema]

    class Config:
        extra = "forbid"


class PlanetExternalSchema(BaseModel):
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


class PlanetsExternalSchema(MainExternalSchema):
    results: List[PlanetExternalSchema]

    class Config:
        extra = "forbid"


class SpecieExternalSchema(BaseModel):
    name: str
    classification: str
    designation: str
    average_height: str
    skin_colors: str
    hair_colors: str
    eye_colors: str
    average_lifespan: str
    homeworld: str = None
    language: str
    people: List[str]
    films: List[str]
    created: str
    edited: str
    url: str

    class Config:
        extra = "forbid"


class SpeciesExternalSchema(MainExternalSchema):
    results: List[SpecieExternalSchema]

    class Config:
        extra = "forbid"


class StarshipExternalSchema(BaseModel):
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


class StarshipsExternalSchema(MainExternalSchema):
    results: List[StarshipExternalSchema]

    class Config:
        extra = "forbid"


class VehicleExternalSchema(BaseModel):
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


class VehiclesExternalSchema(MainExternalSchema):
    results: List[VehicleExternalSchema]

    class Config:
        extra = "forbid"
