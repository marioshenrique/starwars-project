import pytest


@pytest.fixture
def mock_species_data():
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "name": "Human",
                "classification": "mammal",
                "designation": "sentient",
                "average_height": "180",
                "skin_colors": "caucasian, black, asian, hispanic",
                "hair_colors": "blonde, brown, black, red",
                "eye_colors": "brown, blue, green, hazel, grey, amber",
                "average_lifespan": "120",
                "homeworld": "https://swapi.dev/api/planets/9/",
                "language": "Galactic Basic",
                "people": [
                    "https://swapi.dev/api/people/66/",
                    "https://swapi.dev/api/people/67/",
                ],
                "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/2/",
                ],
                "created": "2014-12-10T13:52:11.567000Z",
                "edited": "2014-12-20T21:36:42.136000Z",
                "url": "https://swapi.dev/api/species/1/",
            },
            {
                "name": "Droid",
                "classification": "artificial",
                "designation": "sentient",
                "average_height": "n/a",
                "skin_colors": "n/a",
                "hair_colors": "n/a",
                "eye_colors": "n/a",
                "average_lifespan": "indefinite",
                "homeworld": None,
                "language": "n/a",
                "people": [
                    "https://swapi.dev/api/people/2/",
                    "https://swapi.dev/api/people/3/",
                ],
                "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/2/",
                ],
                "created": "2014-12-10T15:16:16.259000Z",
                "edited": "2014-12-20T21:36:42.139000Z",
                "url": "https://swapi.dev/api/species/2/",
            },
        ],
    }


@pytest.fixture
def mock_specie_data():
    return {
        "name": "Human",
        "classification": "mammal",
        "designation": "sentient",
        "average_height": "180",
        "skin_colors": "caucasian, black, asian, hispanic",
        "hair_colors": "blonde, brown, black, red",
        "eye_colors": "brown, blue, green, hazel, grey, amber",
        "average_lifespan": "120",
        "homeworld": "https://swapi.dev/api/planets/9/",
        "language": "Galactic Basic",
        "people": [
            "https://swapi.dev/api/people/66/",
            "https://swapi.dev/api/people/67/",
        ],
        "films": ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/2/"],
        "created": "2014-12-10T13:52:11.567000Z",
        "edited": "2014-12-20T21:36:42.136000Z",
        "url": "https://swapi.dev/api/species/1/",
    }
