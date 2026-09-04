from fastapi import APIRouter, Depends

from schemas.training_plan import TrainingRequest, TrainingPlan
from services.training_plan import generate_training_plan_service
from settings.security import verify_service_key

router = APIRouter(
    prefix="/training_plans",
    tags=["Training"],
    dependencies=[Depends(verify_service_key)]
)

@router.post("/generate_training_plan", response_model=TrainingPlan)
async def generate_training_plan(request: TrainingRequest) -> TrainingPlan:
    return await generate_training_plan_service(request)
