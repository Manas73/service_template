from starlette.responses import JSONResponse


class {{ cookiecutter.base_error_name }}(Exception):
    """Base Error for the {{ cookiecutter.project_slug }}.

    Args:
        status_code (int): The HTTP status code for this exception.
        message (str): The error message describing the exception.

    Attributes:
        status_code (int): The HTTP status code for this exception.

    """

    def __init__(self, status_code: int, message: str):
        """Initialize the exception with the given status code and message.

        Args:
            status_code (int): The HTTP status code for this exception.
            message (str): The error message describing the exception.

        """
        super().__init__(message)
        self.status_code = status_code

    def get_error_response(self) -> JSONResponse:
        """Returns a JSON response with the exception's status code and message."""
        return JSONResponse(status_code=self.status_code, content={"detail": str(self)})
