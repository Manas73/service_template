from abc import ABC, abstractmethod


class IDatabaseConnection(ABC):
    """An abstract base class for database connections."""

    @abstractmethod
    def get_connection(self):
        """Establish a connection to the database."""
        pass
