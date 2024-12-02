from fastapi import APIRouter, HTTPException, Depends
from schemas.films_schemas import FilmList, Film, FilmIDModel, CharactersFilm
from services.films_service import get_films, get_film_by_id, get_characters_by_film
from schemas.user_schemas import SafeUser
from dependencies.user_dependencies import get_client_user

router = APIRouter(prefix="/films", tags=["films"])


@router.get("", response_model=FilmList)
async def list_films(client: SafeUser = Depends(get_client_user)):
    return await get_films()


@router.get("/{film_id}", response_model=Film)
async def get_film(
    film: FilmIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_film_by_id(film.film_id)


@router.get("/{film_id}/characters", response_model=CharactersFilm)
async def get_characters(
    film: FilmIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_characters_by_film(film.film_id)
