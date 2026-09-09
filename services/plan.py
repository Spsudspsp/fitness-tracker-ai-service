from typing import overload

from schemas.nutrition_plan import NutritionRequest, NutritionPlan
from schemas.training_plan import TrainingPlan, TrainingRequest
from services.provider import get_provider_service


@overload
async def generate_plan_service(request: NutritionRequest) -> NutritionPlan:
    ...

@overload
async def generate_plan_service(request: TrainingRequest) -> TrainingPlan:
    ...

async def generate_plan_service(request: TrainingRequest | NutritionRequest) -> TrainingPlan | NutritionPlan:
    provider = get_provider_service(request)
    return await provider.generate_plan(request)
