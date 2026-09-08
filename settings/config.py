from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    open_ai_api_key: str
    gemini_api_key: str
    service_key: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
