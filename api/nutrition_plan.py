from fastapi import APIRouter, Depends

from schemas.nutrition_plan import NutritionPlan, NutritionRequest
from services.plan import generate_plan_service
from settings.security import verify_service_key

router = APIRouter(
    prefix="/nutrition_plans",
    tags=["Nutrition"],
    dependencies=[Depends(verify_service_key)]
)

@router.post("/generate", response_model=NutritionPlan)
async def generate_nutrition_plan(request: NutritionRequest) -> NutritionPlan:
    return await generate_plan_service(request)
