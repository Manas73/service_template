# Install uv
FROM python:{{ cookiecutter.python_version }}-slim

COPY --from=ghcr.io/astral-sh/uv:0.4.11 /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

# Copy the project into the image
ADD . /app

# Sync the project
RUN uv sync --frozen

EXPOSE 4003

CMD ["/app/.venv/bin/gunicorn", "{{ cookiecutter.pkg_name }}.main:app", "--config", "/app/gunicorn.conf.py"]
