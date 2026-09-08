from providers.gemini import provider as gemini_provider
from providers.open_ai import provider as open_ai_provider
from providers.fake import provider as fake_provider

PROVIDERS = {
    "openai": open_ai_provider,
    "gemini": gemini_provider,
    "fake": fake_provider
}

def get_provider_service(request):
    return PROVIDERS[request.provider]