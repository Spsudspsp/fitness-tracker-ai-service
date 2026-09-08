from schemas.nutrition_plan import NutritionRequest, NutritionPlan
from services.provider import get_provider_service


async def generate_nutrition_plan_service(request: NutritionRequest) -> NutritionPlan:
    provider = get_provider_service(request)
    return await provider.generate_plan(request)
