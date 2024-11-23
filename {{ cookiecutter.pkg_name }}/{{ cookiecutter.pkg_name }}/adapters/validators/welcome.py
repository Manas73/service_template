"""This module contains all validators for the welcome routes."""

from pydantic import BaseModel


class HelloWorldResponse(BaseModel):
    """HelloWorldResponse sends a hello world message."""

    message: str = "Hello World"
