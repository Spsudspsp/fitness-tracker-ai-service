from schemas.training_plan import GeneratedTrainingPlan, GeneratedWorkout, GeneratedWorkoutExercise, TrainingRequest, \
    AvailableExercise


FAKE_REQUEST =TrainingRequest(
        age=30,
        weight_kg=70,
        height_cm=180,
        goal_weight=85,
        experience_level='Intermediate',
        days_per_week=2,
        available_exercises=[
            AvailableExercise(
                id=1,
                name='Squat',
                description='Standard squats, unweighted',
            ),
            AvailableExercise(
                id=2,
                name='Bench press',
                description='Weighted barbell bench press',
            ),
            AvailableExercise(
                id=3,
                name='Bicep curls',
                description='Dumbbell bicep curls',
            ),
            AvailableExercise(
                id=4,
                name='Triceps extensions',
                description='Dumbbell triceps extensions',
            ),
            AvailableExercise(
                id=5,
                name='Shoulder press',
                description='Barbell shoulder press',
            )
        ],
    )


async def generate_training_plan(request: TrainingRequest) -> GeneratedTrainingPlan:
    return GeneratedTrainingPlan(
        name="Test Training Plan",
        description="Test training plan description",
        workouts=[
            GeneratedWorkout(
                day="mon",
                name="Upper Body",
                description="Test upper body workout",
                exercises=[
                    GeneratedWorkoutExercise(
                        exercise_id=1,
                        sets=4,
                        reps=8,
                    ),
                    GeneratedWorkoutExercise(
                        exercise_id=2,
                        sets=3,
                        reps=10,
                    ),
                ],
            ),
            GeneratedWorkout(
                day="wed",
                name="Lower Body",
                description="Test lower body workout",
                exercises=[
                    GeneratedWorkoutExercise(
                        exercise_id=3,
                        sets=4,
                        reps=8,
                    ),
                ],
            ),
        ],
    )
