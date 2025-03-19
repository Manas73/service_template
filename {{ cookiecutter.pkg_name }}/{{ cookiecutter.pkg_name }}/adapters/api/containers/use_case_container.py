from dependency_injector import containers, providers

from {{ cookiecutter.pkg_name }}.settings import ProjectSettings


class UseCaseContainer(containers.DeclarativeContainer):
    """Dependency injection container for the Use Cases."""

    config = providers.Configuration(pydantic_settings=[ProjectSettings()])

    pass
