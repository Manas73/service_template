import logging
from collections.abc import Callable, Generator
from contextlib import contextmanager
from typing import Any

import sqlalchemy
from google.cloud.sql.connector import Connector, IPTypes
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session

from {{ cookiecutter.pkg_name }}.infrastructure.connections.google_cloud_sql_config import GoogleCloudSQLConfig
from {{ cookiecutter.pkg_name }}.infrastructure.connections.interfaces import IMySQLConnection

logger = logging.getLogger("{{ cookiecutter.pkg_name }}")


class GoogleCloudSQLConnection(IMySQLConnection):
    """A class for establishing a connection to a Google Cloud SQL database."""

    def __init__(self, config: GoogleCloudSQLConfig):
        """Initialize the GoogleCloudSQLConnection with the provided configuration."""
        self.config = config
        self.connector = Connector(
            ip_type=IPTypes.PUBLIC,
            timeout=60,
            refresh_strategy="lazy",  # useful when the CPU may be throttled outside of a request context.
            # e.g., Cloud Run, Cloud Functions, etc.
        )
        self.connection = sqlalchemy.create_engine(
            "mysql+pymysql://",
            pool_size=5,
            max_overflow=2,
            pool_recycle=1800,  # maximum number of seconds a connection can persist.
            creator=lambda: self.connector.connect(
                self.config.instance_connection_name,
                "pymysql",
                user=self.config.db_user,
                password=self.config.db_pass,
                db=self.config.db_name,
            ),
        )

    @contextmanager
    def get_connection(self) -> Generator[Session, None, None]:
        """A context manager for managing database connections.

        Yields:
            Session: A SQLAlchemy session.

        """
        session = Session(self.connection, expire_on_commit=False)
        yield session
        session.commit()
        session.close()

    def execute_db_operation(
        self, operation: Callable[[Session], Any], error_message: str = "Database operation error"
    ) -> Any:
        """Execute a database operation within a session and handle any errors.

        Args:
            operation (Callable[[Session], Any]): The database operation to execute.
            error_message (str): The error message to display if the operation fails.
                Defaults to "Database operation error".

        Returns:
            Any: The result of the database operation.

        """
        try:
            with self.get_connection() as session:
                return operation(session)
        except SQLAlchemyError as e:
            logger.error(f"{error_message}: {e}")
            session.rollback()
            raise
