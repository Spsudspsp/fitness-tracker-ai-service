from fastapi import APIRouter

from schemas.training_plan import TrainingRequest, TrainingPlan
from services.training_plan import generate_training_plan_service

router = APIRouter(
    prefix="/training_plans",
    tags=["Training"],
)

@router.post("/generate_training_plan", response_model=TrainingPlan)
async def generate_training_plan(request: TrainingRequest) -> TrainingPlan:
    return await generate_training_plan_service(request)
