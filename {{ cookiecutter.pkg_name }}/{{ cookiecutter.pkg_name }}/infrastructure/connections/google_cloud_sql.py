import sqlalchemy
from google.cloud.sql.connector import Connector

from {{ cookiecutter.pkg_name }}.domain.interfaces import IDatabaseConnection
from {{ cookiecutter.pkg_name }}.infrastructure.connections.google_cloud_sql_config import GoogleCloudSQLConfig


class GoogleCloudSQLConnection(IDatabaseConnection):
    """A class for establishing a connection to a Google Cloud SQL database."""

    def __init__(self, config: GoogleCloudSQLConfig):
        """Initialize the GoogleCloudSQLConnection with the provided configuration."""
        self.config = config
        self.connector = Connector()
        self.connection = sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=lambda: self.connector.connect(
                self.config.instance_connection_name,
                "pymysql",
                user=self.config.db_user,
                password=self.config.db_pass,
                db=self.config.db_name,
            ),
        )

    def get_connection(self) -> sqlalchemy.engine.base.Engine:
        """Returns a connection to the Google Cloud SQL database."""
        return self.connection
