from abc import ABC, abstractmethod
from prompts.builder import PromptBuilder
from schemas.nutrition_plan import NutritionPlan, NutritionRequest
from schemas.training_plan import TrainingRequest, TrainingPlan


class AIProviderBase(ABC):
    prompt_builder = PromptBuilder

    @abstractmethod
    async def generate_plan(self, request):
        pass

    @staticmethod
    def _build_system_prompt():
        return """
        You are a professional fitness assistant.

        Generate a complete weekly or partial workout or nutrition plan based on the user's requirements.

        Only use exercises from the provided list of available exercises.
        Only use ingredients from the provided list of available ingredients.
        Return the exercise and ingredient IDs exactly as provided.
        Do not invent exercises or ingredients.

        Take the user's notes into account when designing the program.
        """

    @classmethod
    def _build_user_prompt(cls, request):
        return cls.prompt_builder.build(request)

    @staticmethod
    def _get_response_schema(request):
        if isinstance(request, TrainingRequest):
            return TrainingPlan
        elif isinstance(request, NutritionRequest):
            return NutritionPlan
        raise TypeError("Invalid plan request type")