import logging
from collections.abc import Callable, Generator
from contextlib import contextmanager
from typing import Any

import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, text

from {{ cookiecutter.pkg_name }}.infrastructure.connections.interfaces import IMySQLConnection

logger = logging.getLogger(__name__)


class MockMySQLConnection(IMySQLConnection):
    """A mock class for simulating a connection to a Google Cloud SQL database using SQLite."""

    def __init__(self, database_name: str):
        """Initialize the MockMySQLConnection with an in-memory SQLite database."""
        self.connection = self._create_engine()
        self._setup_database(database_name)

    def _create_engine(self):
        """Create a SQLAlchemy engine using an in-memory SQLite database."""
        engine = sqlalchemy.create_engine(
            "sqlite:///:memory:",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
        return engine

    @contextmanager
    def get_connection(self) -> Generator[Session, None, None]:
        """A context manager for managing database connections.

        Yields:
            Session: A SQLAlchemy session.
        """
        session = Session(self.connection, expire_on_commit=False)
        try:
            yield session
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            logger.error(f"Database error: {e}")
            raise
        finally:
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
            raise

    def _setup_database(self, database_name: str):
        """Set up the in-memory database for testing."""

        def setup_operation(session):
            session.exec(text(f"ATTACH DATABASE ':memory:' AS '{database_name}';"))  # type: ignore
            SQLModel.metadata.create_all(self.connection)

        self.execute_db_operation(setup_operation, "Error setting up mock database")

    def teardown(self):
        """Tear down the database after testing."""

        def teardown_operation(session):
            SQLModel.metadata.drop_all(self.connection)

        self.execute_db_operation(teardown_operation, "Error tearing down mock database")
