from pydantic import BaseModel, Field
from schemas.plan_request import PlanRequest
from schemas.training_plan import TrainingPlan


# for prompt

class AvailableFoodItem(BaseModel):
    id: str
    name: str = Field(max_length=50)
    calories: int
    carbs: int
    proteins: int
    fats: int


class NutritionRequest(PlanRequest):
    available_food_items: list[AvailableFoodItem]
    training_plan: TrainingPlan | None


# for response

class MealItem(BaseModel):
    food_item_id: str
    quantity: int = Field(ge=1)


class Meal(BaseModel):
    name: str
    ingredients: list[MealItem] = Field(min_length=1)
    typ: str
    day: str


class NutritionPlan(BaseModel):
    name: str
    description: str
    meals: list[Meal] = Field(min_length=1)
