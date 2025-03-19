from collections.abc import Callable
from typing import Any

import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import Client

from {{ cookiecutter.pkg_name }}.infrastructure.connections.firebase_config import FirebaseConfig
from {{ cookiecutter.pkg_name }}.infrastructure.connections.interfaces import IFirebaseConnection


class FirebaseConnection(IFirebaseConnection):
    """A class for connecting to a Google Cloud Firestore database."""

    def __init__(self, config: FirebaseConfig):
        """Initialize the FirebaseConnection with the provided project ID."""
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {"projectId": config.project_id}, name="firestore")
        self.connection = firestore.client()

    def get_connection(self) -> Client:
        """Returns a connection to the Google Cloud Firestore database."""
        return self.connection

    def execute_db_operation(
        self, operation: Callable[[Client], Any], error_message: str = "Firestore operation error"
    ) -> Any:
        """Execute a Firestore operation and handle any errors.

        Args:
            operation (Callable[[firestore.Client], Any]): The Firestore operation to execute.
            error_message (str): The error message to display if the operation fails.

        Returns:
            Any: The result of the Firestore operation.

        """
        return operation(self.connection)
