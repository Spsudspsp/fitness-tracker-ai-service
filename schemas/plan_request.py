from pydantic import BaseModel


class PlanRequest(BaseModel):
    age: int
    weight_kg: float
    height_cm: float
    goal_weight: float
    notes: str = ""
