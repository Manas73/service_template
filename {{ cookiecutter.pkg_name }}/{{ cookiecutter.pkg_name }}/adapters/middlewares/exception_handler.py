from collections.abc import Callable

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from {{ cookiecutter.pkg_name }}.domain.exceptions.{{ cookiecutter.pkg_name }}_error import {{ cookiecutter.base_error_name }}


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    """Middleware for handling exceptions in the analytics service application.

    Attributes:
        app (FastAPI): The FastAPI application instance.

    """

    def __init__(self, app: FastAPI):
        """Initialize the middleware with the FastAPI application instance.

        Args:
            app (FastAPI): The FastAPI application instance.

        """
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Dispatch the request to the next middleware or endpoint and handle exceptions.

        Args:
            request (Request): The incoming request.
            call_next (Callable): The next middleware or endpoint to be called.

        Returns:
            Response: The response from the next middleware or endpoint.
            JSONResponse: A JSON response with a 500 status code and an error message.

        """
        try:
            return await call_next(request)
        except Exception as error:
            if isinstance(error, {{ cookiecutter.base_error_name }}):
                return error.get_error_response()
            raise error
            # return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
