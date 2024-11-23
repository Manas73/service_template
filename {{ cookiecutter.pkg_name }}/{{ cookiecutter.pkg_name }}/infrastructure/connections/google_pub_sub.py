from google.cloud import pubsub_v1

from {{ cookiecutter.pkg_name }}.domain.interfaces import IDatabaseConnection
from {{ cookiecutter.pkg_name }}.infrastructure.connections.google_pubsub_config import GooglePubSubConfig


class GooglePubSubConnection(IDatabaseConnection):
    """A class for connecting to Google Cloud Pub/Sub."""

    def __init__(self, config: GooglePubSubConfig):
        """Initialize the GooglePubSubConnection with the provided configuration."""
        self.config = config
        self.connection = pubsub_v1.PublisherClient()

    def get_connection(self) -> pubsub_v1.PublisherClient:
        """Get the Pub/Sub publisher client connection."""
        return self.connection
