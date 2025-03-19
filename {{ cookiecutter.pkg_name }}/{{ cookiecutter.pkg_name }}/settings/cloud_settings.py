from pydantic_settings import BaseSettings, SettingsConfigDict


class CloudSettings(BaseSettings):
    """Google Cloud configuration settings."""

    PROJECT_ID: str
    STORAGE_BUCKET: str
    JOB_QUEUE_TOPIC_NAME: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    def get_topic_path(self, topic_name: str) -> str:
        """Return the Pub/Sub topic path."""
        return f"projects/{self.PROJECT_ID}/topics/{topic_name}"
