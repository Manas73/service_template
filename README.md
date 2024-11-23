# Service Template

This is a Cookiecutter template for creating a new Python project with a well-structured, modular architecture. It sets up a FastAPI-based application with a clean project structure, including configuration management, API routing, and dependency injection.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python
- [uv](https://github.com/astral-sh/uv) (for dependency management)

## Usage

1. Temporarily Install and run Cookiecutter to generate a new project using this template:

```bash
uvx cookiecutter https://github.com/Manas73/service_template
```

2. You will be prompted to enter various project details. Fill them out according to your preferences.

3. Once the project is generated, navigate to the project directory:

```bash
cd your-project-name
```

4. Set up a virtual environment (optional but recommended):

```bash
uv sync
```

## Project Structure

The generated project will have the following structure:

```
your-project-name/
├── {{ cookiecutter.pkg_name }}/
│   ├── adapters/
│   │   ├── api/
│   │   └── middlewares/
│   ├── config/
│   ├── domain/
│   │   └── entities/
│   ├── infrastructure/
│   ├── use_cases/
│   ├── __init__.py
│   ├── container.py
│   └── main.py
├── tests/
├── README.md
├── pyproject.toml
└── cookiecutter.json
```

## Configuration

The project uses `pyproject.toml` for configuration. You can modify this file to adjust your project settings, including:

- Project metadata (name, version, description)
- Python version requirements
- Dependencies
- Development dependencies
- Linting and formatting tools (ruff, black)
- Testing configuration (pytest)

## Running the Application

To run the application:

```bash
uv run your-project-name.main
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

## API Documentation

Once the server is running, you can access the automatic API documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Testing

To run the tests:

```bash
uv run pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
