from dependency_injector import containers, providers

from {{ cookiecutter.pkg_name }}.settings import AISettings, CloudSettings, DatabaseSettings, SecuritySettings


class InfrastructureContainer(containers.DeclarativeContainer):
    """Dependency injection container for the application's infrastructure components."""

    config = providers.Configuration(
        pydantic_settings=[
            AISettings(),
            CloudSettings(),
            DatabaseSettings(),
            SecuritySettings(),
        ]
    )
    pass
