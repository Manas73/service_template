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

