from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for the service application.

    Attributes:
        PROJECT_ROOT (Path): The absolute path to the project root directory.

    """

    PROJECT_ROOT: Path = Field(default_factory=lambda: Path(__file__).parent.parent.parent.absolute())

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
