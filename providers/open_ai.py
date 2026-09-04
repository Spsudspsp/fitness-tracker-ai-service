from openai import AsyncOpenAI
from schemas.training_plan import GeneratedTrainingPlan, TrainingRequest
from settings.config import settings


class OpenAIProvider:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.ai_api_key)

    async def generate_training_plan(self, request: TrainingRequest) -> GeneratedTrainingPlan:
        res = await self.client.responses.parse(
            model='gpt-5',
            instructions=self._build_system_prompt(),
            input=self._build_user_prompt(request),
            text_format=GeneratedTrainingPlan
        )

        if res.output_parsed is None:
            raise RuntimeError("OpenAI did not return a training plan.")
        return res.output_parsed

    @staticmethod
    def _build_system_prompt() -> str:
        return """
        You are a professional fitness assistant.

        Generate a complete weekly workout plan based on the user's requirements.

        Only use exercises from the provided list of available exercises.
        Return the exercise IDs exactly as provided.

        Take the user's notes into account when designing the program.
        """

    @staticmethod
    def _build_user_prompt(request: TrainingRequest) -> str:
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


provider = OpenAIProvider()
