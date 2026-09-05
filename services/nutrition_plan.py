from schemas.nutrition_plan import MealRequest, NutritionPlan
from providers.fake import provider

async def generate_nutrition_plan_service(request: MealRequest) -> NutritionPlan:
    return await provider.generate_nutrition_plan(request)
