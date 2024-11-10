from fastapi import APIRouter, HTTPException, Depends
from ..serializers.films_serializer import FilmList, Film, FilmIDModel
from ..services.films_service import get_films, get_film_by_id
from ..serializers.user_serializer import SafeUser
from ..dependencies.user_dependencies import get_client_user

router = APIRouter(prefix="/films", tags=["films"])


@router.get("/", response_model=FilmList)
async def list_films(client: SafeUser = Depends(get_client_user)):
    return await get_films()


@router.get("/{film_id}/", response_model=Film)
async def get_film(
    film: FilmIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_film_by_id(film.film_id)
