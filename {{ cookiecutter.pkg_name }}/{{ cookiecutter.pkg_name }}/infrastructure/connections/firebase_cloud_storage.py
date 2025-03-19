from collections.abc import Callable
from typing import Any

import firebase_admin
from firebase_admin import credentials, storage
from google.cloud.storage import Bucket

from {{ cookiecutter.pkg_name }}.infrastructure.connections.firebase_cloud_storage_config import FirebaseCloudStorageConfig
from {{ cookiecutter.pkg_name }}.infrastructure.connections.interfaces import ICloudStorageConnection


class FirebaseCloudStorageConnection(ICloudStorageConnection):
    """A class for connecting to a Firestore Cloud Storage."""

    def __init__(self, config: FirebaseCloudStorageConfig):
        """Initialize the FirebaseCloudStorageConnection with the provided project ID."""
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {"projectId": config.project_id}, name="firestore-storage")
        self.connection = storage.bucket(name=config.storage_bucket)

    def get_connection(self) -> Bucket:
        """Returns a connection to the Firestore Cloud Storage."""
        return self.connection

    def execute_db_operation(
        self, operation: Callable[[Bucket], Any], error_message: str = "Database operation error"
    ) -> Any:
        """Execute a database operation and handle any errors.

        Args:
            operation (Callable[[Bucket], Any]): The database operation to execute.
            error_message (str): The error message to display if the operation fails.
                Defaults to "Database operation error".

        Returns:
            Any: The result of the database operation.

        """
        return operation(self.connection)
