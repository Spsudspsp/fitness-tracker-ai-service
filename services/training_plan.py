from schemas.training_plan import TrainingRequest, TrainingPlan, AvailableExercise
from providers.fake import provider

async def generate_training_plan_service(request: TrainingRequest) -> TrainingPlan:
    return await provider.generate_training_plan(request)
