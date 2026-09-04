from pydantic import BaseModel, Field

# for prompt

class AvailableExercise(BaseModel):
    id: int
    name: str
    description: str


class TrainingRequest(BaseModel):
    age: int
    weight_kg: float
    height_cm: float
    goal_weight: float
    experience_level: str
    days_per_week: int = Field(ge=1, le=7)
    available_exercises: list[AvailableExercise] = Field(min_length=1)
    notes: str = ""

# for response

class GeneratedWorkoutExercise(BaseModel):
    exercise_id: int
    sets: int = Field(ge=1)
    reps: int = Field(ge=1)


class GeneratedWorkout(BaseModel):
    name: str
    exercises: list[GeneratedWorkoutExercise] = Field(min_length=1)
    description: str
    day: str

class GeneratedTrainingPlan(BaseModel):
    name: str
    description: str
    workouts: list[GeneratedWorkout] = Field(min_length=1)
