import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Meta / Instagram
    INSTAGRAM_BUSINESS_ACCOUNT_ID: str = ""
    PAGE_ACCESS_TOKEN: str = ""
    WEBHOOK_VERIFY_TOKEN: str = "insta_ai_verify_token"
    META_APP_SECRET: str = ""

    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o"

    # App
    DEBUG: bool = True
    PORT: int = 8000

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"))

settings = Settings()
