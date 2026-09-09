from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    open_ai_api_key: str
    open_ai_model: str = "gpt-5"

    gemini_api_key: str
    gemini_model: str = "gemini-3.6-flash"

    service_key: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
