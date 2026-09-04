from schemas.training_plan import GeneratedTrainingPlan, GeneratedWorkout, GeneratedWorkoutExercise, TrainingRequest


class FakeProvider:
    async def generate_training_plan(self, request: TrainingRequest) -> GeneratedTrainingPlan:
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

provider = FakeProvider()
