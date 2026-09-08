from schemas.training_plan import TrainingRequest, TrainingPlan, AvailableExercise
from services.provider import get_provider_service


async def generate_training_plan_service(request: TrainingRequest) -> TrainingPlan:
    provider = get_provider_service(request)
    return await provider.generate_plan(request)
