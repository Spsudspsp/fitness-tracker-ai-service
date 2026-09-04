from schemas.training_plan import TrainingRequest, GeneratedTrainingPlan, AvailableExercise
from providers import fake as fake_provider

async def generate_training_plan_service(request: TrainingRequest) -> GeneratedTrainingPlan:
    return await fake_provider.generate_training_plan(request)
