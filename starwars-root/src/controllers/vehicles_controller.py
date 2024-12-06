from fastapi import APIRouter, Depends, status
from schemas.vehicles_schemas import (
    VehiclesListResponse,
    Vehicle,
    VehicleIDModel,
)
from services.vehicles_service import get_vehicles, get_vehicle_by_id

router = APIRouter(prefix="/vehicles", tags=["vehicles"])


@router.get("", response_model=VehiclesListResponse)
async def list_vehicles():
    return await get_vehicles()


@router.get("/{vehicle_id}", response_model=Vehicle)
async def get_vehicle(
    vehicle: VehicleIDModel = Depends()
):
    return await get_vehicle_by_id(vehicle.vehicle_id)
