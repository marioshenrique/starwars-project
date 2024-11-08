from fastapi import APIRouter, HTTPException, Depends
from src.models.films_model import FilmList, Film, FilmIDModel
from src.services.films_service import get_films, get_film_by_id

router = APIRouter(
    prefix="/films",
    tags=["films"]
)

@router.get("/", response_model=FilmList)
async def list_films():
    return await get_films()

@router.get("/{film_id}/", response_model=Film)
async def get_film(film: FilmIDModel = Depends()):
    return await get_film_by_id(film.film_id)