# {{ cookiecutter.project_name }}

## Requirements

- Python {{ cookiecutter.python_version }}
- [uv](https://github.com/astral-sh/uv) (for dependency management)

## Installation

### Local Environment

1. Install Python {{ cookiecutter.python_version }}
   ```shell
   uv python install {{ cookiecutter.python_version }}
   ```

2. Create a virtual environment and install dependencies using UV:
    ```shell
    uv sync
    ```

3. Run the service:
    ```shell
    uv run uvicorn {{ cookiecutter.pkg_name }}.adapters.api.main:app --reload --port 8000
    ```

4. Access the API documentation by opening your web browser and navigate to `http://localhost:8000/docs` to view the Swagger UI for the API.


### Docker

1. Create the network

   ```shell
   docker network create shared
   ```

2. Build the container

   ```shell
   docker build -t {{ cookiecutter.pkg_name }} .
   ```

3. Run the container by using

   ```shell
   docker run --rm -p 4003:4003 {{ cookiecutter.pkg_name }}
   ```
   ​    or

   ```shell
   docker run --rm -p 4003:4003 -e --network host {{ cookiecutter.pkg_name }}
   ```


### Codestyle checks
Commiting code requires it to pass several code checks:
1. **mypy**: A static type checker for Python. It helps catch type-related errors without running the code.
2. **ruff**: Ruff is a Python linter that combines the functionality of flake8, pylint, and other tools. Ruff is configured with specific rules and settings, including:
   - E (flake8 excluding black conflicts)
   - I (isort)
   - N (pep8-naming)
   - D (pydocstyle)
   - UP (pyupgrade)
   - PD (pandas-vet)
   - ANN001 (flake8-annotations missing-type-function-argument)
   - T20 (flake8-print)
   - TID (flake8-tidy-imports)
   - ASYNC (flake8-async)
3. **pytest**: A testing framework for Python. The project uses pytest for running tests and generating coverage reports. Strive to achieve 100% code coverage.
