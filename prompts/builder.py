from schemas.nutrition_plan import NutritionRequest
from schemas.training_plan import TrainingRequest


class PromptBuilder:
    @classmethod
    def build(cls, request):
        if isinstance(request, TrainingRequest):
            return cls._build_training_prompt(request)
        elif isinstance(request, NutritionRequest):
            return cls._build_nutrition_prompt(request)
        raise TypeError("Invalid plan request type")

    @staticmethod
    def _build_training_prompt(request):
        return f"""
            User profile:
            - Age: {request.age}
            - Weight: {request.weight_kg} kg
            - Height: {request.height_cm} cm
            - Goal weight: {request.goal_weight} kg
            - Experience level: {request.experience_level}
            - Days per week: {request.days_per_week}

            Additional instructions:
            {request.notes}

            Available exercises:
            {request.available_exercises}
        """

    @staticmethod
    def _build_nutrition_prompt(request):
        return f"""
            User profile:
            - Age: {request.age}
            - Weight: {request.weight_kg} kg
            - Height: {request.height_cm} cm
            - Goal weight: {request.goal_weight} kg
            
            Additional instructions:
            {request.notes}

            Available food items:
            {request.available_food_items}
            
            User training plan:
            {request.training_plan}
        """
