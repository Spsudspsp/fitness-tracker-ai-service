from openai import AsyncOpenAI

from providers.base import AIProviderBase
from settings.config import settings


class OpenAIProvider(AIProviderBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = AsyncOpenAI(api_key=settings.open_ai_api_key)

    async def generate_plan(self, request):
        response_schema = self._get_response_schema(request)

        res = await self.client.responses.parse(
            model='gpt-5',
            instructions=self._build_system_prompt(),
            input=self._build_user_prompt(request),
            text_format=response_schema
        )

        if res.output_parsed is None:
            raise RuntimeError("OpenAI did not return a training plan.")
        return res.output_parsed


provider = OpenAIProvider()
