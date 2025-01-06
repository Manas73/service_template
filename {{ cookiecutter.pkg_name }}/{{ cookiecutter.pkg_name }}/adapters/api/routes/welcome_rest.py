"""This module contains all welcome REST APIs."""

from fastapi import APIRouter

from {{ cookiecutter.pkg_name }}.adapters.api.validators import HelloWorldResponse

router = APIRouter()


@router.get(
    "/",
    summary="Hello World",
    description='A simple Hello World "GET" route without any authentication',
    response_model=HelloWorldResponse,
)
def hello_world():
    """hello_world route used to check if the server is running.

    This route does not depend on any user authentication.

    Returns:
        A message saying Hello World.

    """
    return HelloWorldResponse()
