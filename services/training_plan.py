from schemas.training_plan import TrainingRequest, GeneratedTrainingPlan, AvailableExercise
from providers.fake import provider

async def generate_training_plan_service(request: TrainingRequest) -> GeneratedTrainingPlan:
    return await provider.generate_training_plan(request)
