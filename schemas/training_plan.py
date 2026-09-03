from typing import Annotated

from pydantic import BaseModel, Field

class TrainingRequest(BaseModel):
    age: int
    weight_kg: float
    height_cm: float
    goal_weight: float
    experience_level: str
    days_per_week: int


class TrainingPlanDay(BaseModel):
    name: str
    description: str


TrainingPlanDayField = Annotated[
    TrainingPlanDay | None,
    Field(default=None, title='The training plan for the day.')
]


class TrainingPlan(BaseModel):
    name: str
    description: str
    mon: TrainingPlanDayField
    tue: TrainingPlanDayField
    wed: TrainingPlanDayField
    thu: TrainingPlanDayField
    fri: TrainingPlanDayField
    sat: TrainingPlanDayField
    sun: TrainingPlanDayField
