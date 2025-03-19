from google.cloud import pubsub_v1

from {{ cookiecutter.pkg_name }}.infrastructure.connections.google_pubsub_config import GooglePubSubConfig
from {{ cookiecutter.pkg_name }}.infrastructure.connections.interfaces.message_queue import IMessageQueue


class GooglePubSubConnection(IMessageQueue):
    """A class for connecting to Google Cloud Pub/Sub."""

    def __init__(self, config: GooglePubSubConfig):
        """Initialize the GooglePubSubConnection with the provided configuration."""
        self.config = config
        self.connection = pubsub_v1.PublisherClient()

    async def publish_message(self, topic: str, message: bytes) -> None:
        """Publish a message to the specified topic."""
        future = self.connection.publish(topic, message)
        future.result(timeout=30)
