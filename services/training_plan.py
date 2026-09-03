from schemas.training_plan import TrainingRequest, TrainingPlan, TrainingPlanDay


async def generate_training_plan_service(request: TrainingRequest) -> TrainingPlan:
    return TrainingPlan(
        name='Test plan name',
        description='Test plan description',
        mon=None,
        tue=TrainingPlanDay(
            name='Test plan mon',
            description='Test plan mon'
        ),
        wed=TrainingPlanDay(
            name='Test plan wed',
            description='Test plan wed'
        ),
        thu=TrainingPlanDay(
            name='Test plan thu',
            description='Test plan thu'
        ),
        fri=None,
        sat=TrainingPlanDay(
            name='Test plan sat',
            description='Test plan sat'
        ),
        sun=None
    )