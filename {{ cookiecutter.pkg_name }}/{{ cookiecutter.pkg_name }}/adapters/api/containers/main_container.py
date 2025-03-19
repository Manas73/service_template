from dependency_injector import containers, providers

from {{ cookiecutter.pkg_name }}.adapters.api.containers.infrastructure_container import InfrastructureContainer
from {{ cookiecutter.pkg_name }}.adapters.api.containers.repository_container import RepositoryContainer
from {{ cookiecutter.pkg_name }}.adapters.api.containers.use_case_container import UseCaseContainer


class Container(containers.DeclarativeContainer):
    """Dependency injection container for the analytics service application."""

    wiring_config = containers.WiringConfiguration(
        modules=[
            "{{ cookiecutter.pkg_name }}.adapters.api.routes.v1.sample_endpoint",
        ]
    )

    infrastructure = providers.Container(InfrastructureContainer)
    infrastructure.check_dependencies()

    repositories = providers.Container(RepositoryContainer)
    repositories.check_dependencies()

    use_cases = providers.Container(UseCaseContainer)
    use_cases.check_dependencies()
