from {{ cookiecutter.pkg_name }}.domain.exceptions.{{ cookiecutter.pkg_name }}_error import {{ cookiecutter.base_error_name }}


def get_fastapi_error_response(
        errors: list[{{ cookiecutter.base_error_name }}],
        successful_response: dict = None,
) -> dict[int, dict]:
    """Generates a dictionary of FastAPI error responses based on a list of {{ cookiecutter.base_error_name }}.

    Args:
        errors (list[{{ cookiecutter.base_error_name }}]): A list of {{ cookiecutter.base_error_name }}.
        successful_response (dict, optional): A successful response. Defaults to None.

    Returns:
        dict[int, dict]: A dictionary of FastAPI error responses.

    """
    responses = {
        error.status_code: {"content": {"application/json": {"example": {"detail": str(error)}}}} for error in errors
    }

    responses[500] = {"content": {"application/json": {"example": {"detail": "Internal Server Error"}}}}

    if successful_response:
        responses[200] = {"content": {"application/json": {"example": successful_response}}}

    return responses
