# {{ cookiecutter.project_name }}

## Requirements

- Python {{ cookiecutter.python_version }}
- [uv](https://github.com/astral-sh/uv) (for dependency management)

## Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}.git
    cd {{ cookiecutter.pkg_name }}
    ```

2. Create a virtual environment and install dependencies using UV:
    ````shell
    uv sync
    ````

## Starting the API Service

To start the API service using Docker, follow these steps:

1. Build the Docker image:
    ```shell
    docker build -f api_service.Dockerfile -t {{ cookiecutter.pkg_name }} .
    ```

2. Run the Docker container:
    ```shell
    docker run --rm -p 4003:4003 {{ cookiecutter.pkg_name }}:latest
    ```

3. Access the API by navigating to: [http://0.0.0.0:4003](http://0.0.0.0:4003)

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
