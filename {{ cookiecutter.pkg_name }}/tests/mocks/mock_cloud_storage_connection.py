from collections.abc import Callable
from io import BytesIO
from typing import Any

from google.api_core.exceptions import NotFound
from google.cloud.storage import Bucket

from {{ cookiecutter.pkg_name }}.infrastructure.connections.firebase_cloud_storage_config import FirebaseCloudStorageConfig
from {{ cookiecutter.pkg_name }}.infrastructure.connections.interfaces import ICloudStorageConnection


class MockBlob:
    """Mock implementation of Google Cloud Storage Blob."""

    def __init__(self, name: str, bucket: "MockBucket"):
        self.name = name
        self.bucket = bucket
        self._content = ""
        self._exists = False
        self.public_url = f"https://storage.googleapis.com/{bucket.name}/{name}"

    def exists(self) -> bool:
        """Check if the blob exists."""
        return self._exists

    def upload_from_string(self, data: str, content_type: str | None = None) -> None:
        """Upload data from a string."""
        self._content = data
        self._exists = True

    def upload_from_file(self, file_obj: Any, content_type: str | None = None) -> None:
        """Upload data from a file-like object."""
        self._content = file_obj.read()
        file_obj.seek(0)  # Reset file position
        self._exists = True

    def download_as_text(self) -> str:
        """Download the blob content as text."""
        if not self._exists:
            raise NotFound(f"Blob {self.name} not found")
        return self._content

    def make_public(self) -> None:
        """Make the blob publicly accessible."""
        pass


class MockBucket:
    """Mock implementation of Google Cloud Storage Bucket."""

    def __init__(self, name: str):
        self.name = name
        self._blobs: dict[str, MockBlob] = {}

    def blob(self, name: str) -> MockBlob:
        """Get a blob object by name."""
        if name not in self._blobs:
            self._blobs[name] = MockBlob(name, self)
        return self._blobs[name]

    def list_blobs(self, prefix: str = "") -> list[MockBlob]:
        """List blobs with the given prefix."""
        return [blob for name, blob in self._blobs.items() if name.startswith(prefix) and blob.exists()]


class MockCloudStorageConnection(ICloudStorageConnection):
    """Mock implementation of Cloud Storage Connection for testing."""

    def __init__(self, config: FirebaseCloudStorageConfig):
        """Initialize the MockCloudStorageConnection.

        Args:
            config (FirebaseCloudStorageConfig): The configuration for the connection.
        """
        self.config = config
        self.connection = MockBucket(config.storage_bucket)

    def get_connection(self) -> MockBucket:
        """Get the mock bucket connection."""
        return self.connection

    def execute_db_operation(
        self, operation: Callable[[Bucket], Any], error_message: str = "Database operation error"
    ) -> Any:
        """Execute a database operation with the mock bucket.

        Args:
            operation (Callable[[Bucket], Any]): The operation to execute.
            error_message (str): Error message to use if the operation fails.

        Returns:
            Any: The result of the operation.
        """
        return operation(self.connection)

    def set_mock_data(self, blob_name: str, content: str) -> None:
        """Set mock data for a blob.

        Args:
            blob_name (str): The name of the blob.
            content (str): The content to set.
        """
        blob = self.connection.blob(blob_name)
        blob.upload_from_string(content)

    def set_mock_file(self, blob_name: str, content: bytes) -> None:
        """Set mock file data for a blob.

        Args:
            blob_name (str): The name of the blob.
            content (bytes): The content to set.
        """
        blob = self.connection.blob(blob_name)
        blob.upload_from_file(BytesIO(content))
