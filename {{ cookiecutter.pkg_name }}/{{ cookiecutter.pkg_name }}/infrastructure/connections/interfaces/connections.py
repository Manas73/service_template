from abc import ABC

from google.cloud.firestore_v1 import Client as FirestoreClient
from google.cloud.storage import Client as StorageClient
from sqlmodel import Session

from {{ cookiecutter.pkg_name }}.infrastructure.connections.interfaces.database_connection import IDatabaseConnection


class IFirebaseConnection(IDatabaseConnection[FirestoreClient], ABC):
    """Interface for Firebase Firestore connections."""

    pass


class IMySQLConnection(IDatabaseConnection[Session], ABC):
    """Interface for MySQL database connections."""

    pass


class ICloudStorageConnection(IDatabaseConnection[StorageClient], ABC):
    """Interface for Google Cloud Storage connections."""

    pass
