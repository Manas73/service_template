from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Configuration settings for the database..

    Attributes:
        INSTANCE_CONNECTION_NAME (str): The name of the Cloud SQL instance connection.

    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    def get_db_uri(self) -> str:
        """Return the database URI."""
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
