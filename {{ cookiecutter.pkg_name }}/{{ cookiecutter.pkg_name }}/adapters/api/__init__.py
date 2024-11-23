"""This module contains all the routers for the APIs."""

from {{ cookiecutter.pkg_name }}.adapters.api.versions import v1_router
from {{ cookiecutter.pkg_name }}.adapters.api.welcome_rest import router as welcome_router
