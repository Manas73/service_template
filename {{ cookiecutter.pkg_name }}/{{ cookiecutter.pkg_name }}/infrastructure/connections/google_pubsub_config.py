class GooglePubSubConfig:
    """Configuration settings for Google Cloud Pub/Sub."""

    def __init__(self, project_id: str) -> None:
        """Initialize the GooglePubSubConfig with the provided project ID and topic name."""
        self.project_id = project_id
