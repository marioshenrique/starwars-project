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
                "homeworld": "https://example.com/planets/9/",
                "language": "Galactic Basic",
                "people": [
                    "https://example.com/people/66/",
                    "https://example.com/people/67/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-10T13:52:11.567000Z",
                "edited": "2014-12-20T21:36:42.136000Z",
                "url": "https://example.com/species/1/",
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
                    "https://example.com/people/2/",
                    "https://example.com/people/3/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-10T15:16:16.259000Z",
                "edited": "2014-12-20T21:36:42.139000Z",
                "url": "https://example.com/species/2/",
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
        "homeworld": "https://example.com/planets/9/",
        "language": "Galactic Basic",
        "people": [
            "https://example.com/people/66/",
            "https://example.com/people/67/",
        ],
        "films": ["https://example.com/films/1/", "https://example.com/films/2/"],
        "created": "2014-12-10T13:52:11.567000Z",
        "edited": "2014-12-20T21:36:42.136000Z",
        "url": "https://example.com/species/1/",
    }


@pytest.fixture
def mock_get_data_of_test_get_species_by_id_success():
    return {
        "name": "Human",
        "classification": "mammal",
        "designation": "sentient",
        "average_height": "180",
        "skin_colors": "caucasian, black, asian, hispanic",
        "hair_colors": "blonde, brown, black, red",
        "eye_colors": "brown, blue, green, hazel, grey, amber",
        "average_lifespan": "120",
        "homeworld": "https://example.com/planets/1/",
        "language": "Galactic Basic",
        "people": [
            "https://example.com/people/1/",
            "https://example.com/people/2/",
        ],
        "films": [
            "https://example.com/films/1/",
            "https://example.com/films/2/",
            "https://example.com/films/3/",
        ],
        "created": "2014-12-10T13:52:11.567000Z",
        "edited": "2014-12-20T21:36:42.136000Z",
        "url": "https://example.com/species/1/",
    }


@pytest.fixture
def mock_get_data_list_of_test_get_species_success():
    return (
        None,
        2,
        [
            {
                "name": "Human",
                "classification": "mammal",
                "designation": "sentient",
                "average_height": "180",
                "skin_colors": "caucasian, black, asian, hispanic",
                "hair_colors": "blonde, brown, black, red",
                "eye_colors": "brown, blue, green, hazel, grey, amber",
                "average_lifespan": "120",
                "homeworld": "https://example.com/planets/1/",
                "language": "Galactic Basic",
                "people": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                    "https://example.com/films/3/",
                ],
                "created": "2014-12-10T13:52:11.567000Z",
                "edited": "2014-12-20T21:36:42.136000Z",
                "url": "https://example.com/species/1/",
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
                "homeworld": "null",
                "language": "n/a",
                "people": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                    "https://example.com/films/3/",
                ],
                "created": "2014-12-10T13:52:11.567000Z",
                "edited": "2014-12-20T21:36:42.136000Z",
                "url": "https://example.com/species/2/",
            },
        ],
    )


@pytest.fixture
def mock_get_correlated_data_of_test_get_people_by_specie_success():
    return {
        "count": 2,
        "people": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "mass": "77",
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male",
                "homeworld": "https://example.com/planets/1/",
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "species": ["https://example.com/species/1/"],
                "vehicles": [
                    "https://example.com/vehicles/1/",
                    "https://example.com/vehicles/2/",
                ],
                "starships": [
                    "https://example.com/starships/1/",
                    "https://example.com/starships/2/",
                ],
                "created": "2014-12-09T13:50:51.644000Z",
                "edited": "2014-12-20T21:17:56.891000Z",
                "url": "https://example.com/people/1/",
            },
            {
                "name": "C-3PO",
                "height": "167",
                "mass": "75",
                "hair_color": "n/a",
                "skin_color": "gold",
                "eye_color": "yellow",
                "birth_year": "112BBY",
                "gender": "n/a",
                "homeworld": "https://example.com/planets/1/",
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "species": ["https://example.com/species/1/"],
                "vehicles": [
                    "https://example.com/vehicles/1/",
                    "https://example.com/vehicles/2/",
                ],
                "starships": [
                    "https://example.com/starships/1/",
                    "https://example.com/starships/2/",
                ],
                "created": "2014-12-10T15:10:51.357000Z",
                "edited": "2014-12-20T21:17:50.309000Z",
                "url": "https://example.com/people/2/",
            },
        ],
    }


@pytest.fixture
def mock_get_correlated_data_of_test_get_films_by_specie_success():
    return {
        "count": 2,
        "films": [
            {
                "title": "A New Hope",
                "episode_id": 4,
                "opening_crawl": "Lorem ipsum quis potenti tortor imperdiet, nibh egestas habitasse vulputate.",
                "director": "George Lucas",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1977-05-25",
                "characters": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                    "https://example.com/people/3/",
                ],
                "planets": [
                    "https://example.com/planets/1/",
                    "https://example.com/planets/2/",
                    "https://example.com/planets/3/",
                ],
                "starships": [
                    "https://example.com/starships/1/",
                    "https://example.com/starships/2/",
                ],
                "vehicles": [
                    "https://example.com/vehicles/1/",
                ],
                "species": [
                    "https://example.com/species/1/",
                    "https://example.com/species/2/",
                    "https://example.com/species/3/",
                    "https://example.com/species/4/",
                ],
                "created": "2014-12-10T14:23:31.880000Z",
                "edited": "2014-12-20T19:49:45.256000Z",
                "url": "https://example.com/films/1/",
            },
            {
                "title": "The Empire Strikes Back",
                "episode_id": 5,
                "opening_crawl": "Lorem ipsum quis potenti tortor imperdiet, nibh egestas habitasse vulputate.",
                "director": "Irvin Kershner",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1980-05-17",
                "characters": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                ],
                "planets": [
                    "https://example.com/planets/1/",
                    "https://example.com/planets/2/",
                    "https://example.com/planets/3/",
                ],
                "starships": [
                    "https://example.com/starships/1/",
                    "https://example.com/starships/2/",
                    "https://example.com/starships/3/",
                    "https://example.com/starships/4/",
                ],
                "vehicles": [
                    "https://example.com/vehicles/1/",
                    "https://example.com/vehicles/2/",
                    "https://example.com/vehicles/3/",
                    "https://example.com/vehicles/4/",
                    "https://example.com/vehicles/5/",
                ],
                "species": [
                    "https://example.com/species/1/",
                    "https://example.com/species/2/",
                ],
                "created": "2014-12-12T11:26:24.656000Z",
                "edited": "2014-12-15T13:07:53.386000Z",
                "url": "https://example.com/films/2/",
            },
        ],
    }
