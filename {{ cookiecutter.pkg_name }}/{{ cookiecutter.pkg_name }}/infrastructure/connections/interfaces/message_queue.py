from abc import ABC, abstractmethod


class IMessageQueue(ABC):
    """An abstract base class for message queues."""

    @abstractmethod
    async def publish_message(self, topic: str, message: bytes) -> None:
        """Publish a message to the specified topic."""
        pass
