from google import genai
from providers.base import AIProviderBase
from settings.config import settings


class GeminiProvider(AIProviderBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = genai.Client(api_key=settings.gemini_api_key)

    async def generate_plan(self, request):
        response_schema = self._get_response_schema(request)

        res = self.client.models.generate_content(
            model='gemini-3.6-flash',
            contents=self._build_user_prompt(request),
            config=genai.types.GenerateContentConfig(
                system_instruction=self._build_system_prompt(),
                response_mime_type='application/json',
                response_schema=response_schema
            )
        )

        if res.text is None:
            raise RuntimeError("Gemini did not return a training plan.")
        return response_schema.model_validate_json(res.text)

provider = GeminiProvider()
