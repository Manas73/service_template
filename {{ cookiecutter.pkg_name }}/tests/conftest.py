import pytest

monkeypatch = pytest.MonkeyPatch()

# Monkey patch the environment variable so that we can test dependencies.
monkeypatch.setenv("SAMPLE_ENV_VARIABLE", "")
