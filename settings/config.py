from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ai_api_key: str
    service_key: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
