from fastapi import APIRouter, Depends

from schemas.nutrition_plan import NutritionPlan, MealRequest
from services.nutrition_plan import generate_nutrition_plan_service
from settings.security import verify_service_key

router = APIRouter(
    prefix="/nutrition_plans",
    tags=["Nutrition"],
    dependencies=[Depends(verify_service_key)]
)

@router.post("/generate_nutrition_plan", response_model=NutritionPlan)
async def generate_nutrition_plan(request: MealRequest) -> NutritionPlan:
    return await generate_nutrition_plan_service(request)