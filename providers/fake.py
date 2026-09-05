from schemas.nutrition_plan import MealRequest, NutritionPlan, Meal, MealItem
from schemas.training_plan import TrainingPlan, Workout, WorkoutExercise, TrainingRequest


class FakeProvider:
    async def generate_training_plan(self, request: TrainingRequest) -> TrainingPlan:
        return TrainingPlan(
            name="Test Training Plan",
            description="Test training plan description",
            workouts=[
                Workout(
                    day="mon",
                    name="Upper Body",
                    description="Test upper body workout",
                    exercises=[
                        WorkoutExercise(
                            exercise_id=1,
                            sets=4,
                            reps=8,
                        ),
                        WorkoutExercise(
                            exercise_id=2,
                            sets=3,
                            reps=10,
                        ),
                    ],
                ),
                Workout(
                    day="wed",
                    name="Lower Body",
                    description="Test lower body workout",
                    exercises=[
                        WorkoutExercise(
                            exercise_id=3,
                            sets=4,
                            reps=8,
                        ),
                    ],
                ),
            ],
        )

    async def generate_nutrition_plan(self, request: MealRequest) -> NutritionPlan:
        return NutritionPlan(
            name="Test Nutrition Plan",
            description="Test meal plan description",
            meals=[
                Meal(
                    name="Test Meal 1",
                    typ='breakfast',
                    day="mon",
                    ingredients=[
                        MealItem(
                            food_item_id=1,
                            quantity=100,
                        ),
                        MealItem(
                            food_item_id=2,
                            quantity=80,
                        )
                    ]
                ),
                Meal(
                    name="Test Meal 2",
                    typ='lunch',
                    day="tue",
                    ingredients=[
                        MealItem(
                            food_item_id=3,
                            quantity=150,
                        ),
                        MealItem(
                            food_item_id=4,
                            quantity=50,
                        ),
                        MealItem(
                            food_item_id=5,
                            quantity=35,
                        ),
                    ]
                ),
            ]
        )

provider = FakeProvider()
