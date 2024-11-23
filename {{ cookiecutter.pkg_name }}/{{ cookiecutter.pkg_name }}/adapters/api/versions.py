"""V1 endpoint routes."""

from fastapi import APIRouter
from {{ cookiecutter.pkg_name }}.adapters.api.v1 import sample_endpoint_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(sample_endpoint_router, tags=["Sample Endpoint"])


