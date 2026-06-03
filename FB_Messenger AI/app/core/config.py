import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Facebook / Messenger
    PAGE_ID: str = ""
    PAGE_ACCESS_TOKEN: str = ""
    WEBHOOK_VERIFY_TOKEN: str = "messenger_ai_verify_token"
    META_APP_SECRET: str = ""

    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o"

    # App
    DEBUG: bool = True
    PORT: int = 8001

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"))

settings = Settings()
