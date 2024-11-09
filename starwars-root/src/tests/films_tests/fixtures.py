import pytest


@pytest.fixture
def mock_films_data():
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "title": "A New Hope",
                "episode_id": 4,
                "opening_crawl": "It is a period of civil war.",
                "director": "George Lucas",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1977-05-25",
                "characters": [
                    "https://swapi.dev/api/people/1/",
                    "https://swapi.dev/api/people/2/",
                ],
                "planets": [
                    "https://swapi.dev/api/planets/1/",
                    "https://swapi.dev/api/planets/2/",
                ],
                "starships": [
                    "https://swapi.dev/api/starships/2/",
                    "https://swapi.dev/api/starships/3/",
                ],
                "vehicles": [
                    "https://swapi.dev/api/vehicles/4/",
                    "https://swapi.dev/api/vehicles/6/",
                ],
                "species": [
                    "https://swapi.dev/api/species/1/",
                    "https://swapi.dev/api/species/2/",
                ],
                "created": "2014-12-10T14:23:31.880000Z",
                "edited": "2014-12-20T19:49:45.256000Z",
                "url": "https://swapi.dev/api/films/1/",
            },
            {
                "title": "The Empire Strikes Back",
                "episode_id": 5,
                "opening_crawl": "It is a dark time for the\r\nRebellion.",
                "director": "Irvin Kershner",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1980-05-17",
                "characters": [
                    "https://swapi.dev/api/people/1/",
                    "https://swapi.dev/api/people/2/",
                ],
                "planets": [
                    "https://swapi.dev/api/planets/4/",
                    "https://swapi.dev/api/planets/5/",
                ],
                "starships": [
                    "https://swapi.dev/api/starships/3/",
                    "https://swapi.dev/api/starships/10/",
                ],
                "vehicles": [
                    "https://swapi.dev/api/vehicles/8/",
                    "https://swapi.dev/api/vehicles/14/",
                ],
                "species": [
                    "https://swapi.dev/api/species/1/",
                    "https://swapi.dev/api/species/2/",
                ],
                "created": "2014-12-12T11:26:24.656000Z",
                "edited": "2014-12-15T13:07:53.386000Z",
                "url": "https://swapi.dev/api/films/2/",
            },
        ],
    }


@pytest.fixture
def mock_film_data():
    return {
        "title": "A New Hope",
        "episode_id": 4,
        "opening_crawl": "It is a period of civil war",
        "director": "George Lucas",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1977-05-25",
        "characters": [
            "https://swapi.dev/api/people/1/",
            "https://swapi.dev/api/people/2/",
        ],
        "planets": [
            "https://swapi.dev/api/planets/1/",
            "https://swapi.dev/api/planets/2/",
        ],
        "starships": [
            "https://swapi.dev/api/starships/2/",
            "https://swapi.dev/api/starships/3/",
        ],
        "vehicles": [
            "https://swapi.dev/api/vehicles/4/",
            "https://swapi.dev/api/vehicles/6/",
        ],
        "species": [
            "https://swapi.dev/api/species/1/",
            "https://swapi.dev/api/species/2/",
        ],
        "created": "2014-12-10T14:23:31.880000Z",
        "edited": "2014-12-20T19:49:45.256000Z",
        "url": "https://swapi.dev/api/films/1/",
    }
