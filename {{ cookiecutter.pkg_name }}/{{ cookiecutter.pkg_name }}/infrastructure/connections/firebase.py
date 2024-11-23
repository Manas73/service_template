import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import Client

from {{ cookiecutter.pkg_name }}.domain.interfaces import IDatabaseConnection
from {{ cookiecutter.pkg_name }}.infrastructure.connections.firebase_config import FirebaseConfig


class FirebaseConnection(IDatabaseConnection):
    """A class for connecting to a Google Cloud Firestore database."""

    def __init__(self, config: FirebaseConfig):
        """Initialize the FirebaseConnection with the provided project ID."""
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {"projectId": config.project_id}, name="firestore")
        self.connection = firestore.client()

    def get_connection(self) -> Client:
        """Returns a connection to the Google Cloud Firestore database."""
        return self.connection
