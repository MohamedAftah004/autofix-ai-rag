from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LLM_BASE_URL: str = "http://localhost:1234/v1"
    LLM_API_KEY: str = "lm-studio"
    LLM_MODEL: str = "qwen2.5-7b-instruct"


settings = Settings()