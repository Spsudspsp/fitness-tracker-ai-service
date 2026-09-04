from schemas.training_plan import TrainingRequest, GeneratedTrainingPlan
from providers import fake as fake_provider

async def generate_training_plan_service(request: TrainingRequest) -> GeneratedTrainingPlan:
    prompt = ''
    return await fake_provider.generate_plan(prompt)
