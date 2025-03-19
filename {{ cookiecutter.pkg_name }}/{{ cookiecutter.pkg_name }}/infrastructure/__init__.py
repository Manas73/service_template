"""Infrastructure module for {{ cookiecutter.project_name }}.

This module contains all infrastructure components including connections, external services,
repositories, and services required by the application.
"""

# Import connections
{%- if cookiecutter.include_database == 'yes' %}
from {{ cookiecutter.pkg_name }}.infrastructure.connections import (
    DatabaseConfig,
    DatabaseConnection,
)
{%- endif %}

{%- if cookiecutter.include_cloud_storage == 'yes' %}
from {{ cookiecutter.pkg_name }}.infrastructure.connections import (
    CloudStorageConfig,
    CloudStorageConnection,
)
{%- endif %}

{%- if cookiecutter.include_pubsub == 'yes' %}
from {{ cookiecutter.pkg_name }}.infrastructure.connections import (
    PubSubConfig,
    PubSubConnection,
)
{%- endif %}

{%- if cookiecutter.include_firebase == 'yes' %}
from {{ cookiecutter.pkg_name }}.infrastructure.connections import (
    FirebaseConfig,
    FirebaseConnection,
)
{%- endif %}

# Import external services
{%- if cookiecutter.include_llm_integration == 'yes' %}
from {{ cookiecutter.pkg_name }}.infrastructure.external_services import LLMFactory
{%- endif %}

# Import repositories
# Add your repository imports here as needed

# Import services
# Add your service imports here as needed