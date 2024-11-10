from fastapi import APIRouter, Depends, status
from ..serializers.vehicles_serializer import (
    VehiclesListResponse,
    Vehicles,
    VehiclesIDModel,
)
from ..services.vehicles_service import get_vehicles, get_vehicle_by_id
from ..serializers.user_serializer import SafeUser
from ..dependencies.user_dependencies import get_client_user

router = APIRouter(prefix="/vehicles", tags=["vehicles"])


@router.get("/", response_model=VehiclesListResponse)
async def list_vehicles(client: SafeUser = Depends(get_client_user)):
    return await get_vehicles()


@router.get("/{vehicle_id}/", response_model=Vehicles)
async def get_vehicle(
    vehicle: VehiclesIDModel = Depends(), client: SafeUser = Depends(get_client_user)
):
    return await get_vehicle_by_id(vehicle.vehicle_id)
