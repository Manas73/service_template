"""This module is used for demonstration purpose as part of the template and contains a sample API."""

from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/sample",
    summary="Sample API",
    description="A Sample API endpoint.",
    responses={
        200: {"content": {"application/json": {"example": {"message": "Sample Response"}}}},
    },
)
def sample_api():
    """sample_api route is used for demonstration purpose as part of the template.

    Returns:
        A message saying Sample Response.

    """
    return {"message": "Sample Response"}
