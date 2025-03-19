from collections import defaultdict
from collections.abc import Callable
from typing import Any
from unittest.mock import Mock

from google.cloud.firestore_v1 import Client

from {{ cookiecutter.pkg_name }}.infrastructure.connections.firebase_config import FirebaseConfig
from {{ cookiecutter.pkg_name }}.infrastructure.connections.interfaces import IFirebaseConnection


class MockDocumentReference:
    def __init__(self, parent, doc_id):
        self.parent = parent
        self.id = doc_id

    def get(self):
        return self.parent.parent.mock_get(self.parent.collection_name, self.id)

    def update(self, update_data):
        return self.parent.parent.mock_update(self.parent.collection_name, self.id, update_data)

    def set(self, set_data, merge=False):
        return self.parent.parent.mock_set(self.parent.collection_name, self.id, set_data, merge)


class MockCollectionReference:
    def __init__(self, parent, collection_name):
        self.parent = parent
        self.collection_name = collection_name

    def document(self, doc_id=None):
        # create random doc_id if not provided
        if doc_id is None:
            doc_id = f"random_doc_id_{len(self.parent.mock_data.get(self.collection_name, {}))}"

        return MockDocumentReference(self, doc_id)

    def where(self, *args, **kwargs):
        return self

    def limit(self, *args, **kwargs):
        return self

    def stream(self):
        return self.parent.mock_stream(self.collection_name)

    def order_by(self, *args, **kwargs):
        return self

    def offset(self, *args, **kwargs):
        return self

    def get(self):
        return self.parent.mock_stream(self.collection_name)


class MockFirebaseConnection(IFirebaseConnection):
    def __init__(self, config: FirebaseConfig):
        self.config = config
        self.mock_client = Mock(spec=Client)
        self.mock_data: dict[str, dict[str, Any]] = defaultdict(dict)
        self.collection_name = None
        self.setup_mock_client()

    def get_connection(self) -> Client:
        return self.mock_client

    def execute_db_operation(
        self, operation: Callable[[Client], Any], error_message: str = "Database operation error"
    ) -> Any:
        return operation(self.mock_client)

    def setup_mock_client(self):
        self.mock_client.collection = self.collection

    def set_mock_data(self, collection: str, doc_id: str, data: dict):
        self.mock_data[collection][doc_id] = data

    def get_mock_data(self, collection: str, doc_id: str) -> dict | None:
        return self.mock_data[collection].get(doc_id)

    def collection(self, collection_name):
        return MockCollectionReference(self, collection_name)

    def mock_get(self, collection_name, doc_id):
        mock_doc = Mock()
        mock_doc.exists = False

        if self.mock_data[collection_name].get(doc_id):
            mock_doc.exists = True
            mock_doc.to_dict.return_value = self.mock_data[collection_name][doc_id]

        return mock_doc

    def mock_update(self, collection_name, doc_id, update_data):
        if doc_id not in self.mock_data[collection_name]:
            self.mock_data[collection_name][doc_id] = {}

        self.mock_data[collection_name][doc_id].update(update_data)

    def mock_set(self, collection_name, doc_id, set_data, merge=False):
        if merge and doc_id in self.mock_data[collection_name]:
            self.mock_data[collection_name][doc_id].update(set_data)
        else:
            self.mock_data[collection_name][doc_id] = set_data

    def mock_stream(self, collection_name):
        for doc_id, data in self.mock_data[collection_name].items():
            mock_doc = Mock()
            mock_doc.to_dict.return_value = data
            yield mock_doc
