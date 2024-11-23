import firebase_admin
from firebase_admin import credentials, storage
from google.cloud.storage import Bucket

from {{ cookiecutter.pkg_name }}.domain.interfaces import IDatabaseConnection
from {{ cookiecutter.pkg_name }}.infrastructure.connections.firebase_cloud_storage_config import (
    FirebaseCloudStorageConfig,
)


class FirebaseCloudStorageConnection(IDatabaseConnection):
    """A class for connecting to a Firestore Cloud Storage."""

    def __init__(self, config: FirebaseCloudStorageConfig):
        """Initialize the FirebaseCloudStorageConnection with the provided project ID."""
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {"projectId": config.project_id}, name="firestore-storage")
        self.connection = storage.bucket(name=config.storage_bucket)

    def get_connection(self) -> Bucket:
        """Returns a connection to the Firestore Cloud Storage."""
        return self.connection
