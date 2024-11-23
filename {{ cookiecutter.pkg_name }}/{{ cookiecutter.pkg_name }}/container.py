from dependency_injector import containers, providers

from {{ cookiecutter.pkg_name }}.config.settings import Settings


class Container(containers.DeclarativeContainer):
    """Dependency injection container for the analytics service application.

    Attributes:
        wiring_config (WiringConfiguration): Configuration for wiring modules.
        settings_provider (Singleton): Provider for the application settings.
        config (Settings): Application settings.

    """

    wiring_config = containers.WiringConfiguration(
        modules=[
            "{{ cookiecutter.pkg_name }}.adapters.api.v1.sample_endpoint",
        ]
    )
    settings_provider = providers.Singleton(Settings)
    config = settings_provider()


