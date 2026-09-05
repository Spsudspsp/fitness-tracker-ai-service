from pydantic import BaseModel, Field
from schemas.plan_request import PlanRequest


# for prompt

class AvailableExercise(BaseModel):
    id: int
    name: str
    description: str


class TrainingRequest(PlanRequest):
    experience_level: str
    days_per_week: int = Field(ge=1, le=7)
    available_exercises: list[AvailableExercise] = Field(min_length=1)

# for response

class WorkoutExercise(BaseModel):
    exercise_id: int
    sets: int = Field(ge=1)
    reps: int = Field(ge=1)


class Workout(BaseModel):
    name: str
    exercises: list[WorkoutExercise] = Field(min_length=1)
    description: str
    day: str


class TrainingPlan(BaseModel):
    name: str
    description: str
    workouts: list[Workout] = Field(min_length=1)
