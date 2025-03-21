from pydantic_settings import BaseSettings, SettingsConfigDict


class AISettings(BaseSettings):
    """AI configuration settings."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
