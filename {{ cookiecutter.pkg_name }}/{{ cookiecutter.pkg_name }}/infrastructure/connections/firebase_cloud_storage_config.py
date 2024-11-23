from {{ cookiecutter.pkg_name }}.infrastructure.connections.firebase_config import FirebaseConfig


class FirebaseCloudStorageConfig(FirebaseConfig):
    """A class to hold Firebase configuration parameters."""

    def __init__(self, project_id: str, storage_bucket: str):
        """Initialize the FirebaseConfig with the provided project ID."""
        super().__init__(project_id)
        self.storage_bucket = storage_bucket
