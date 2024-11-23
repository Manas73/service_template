class GoogleCloudSQLConfig:
    """A class to hold database configuration parameters."""

    def __init__(self, instance_connection_name: str, db_user: str, db_pass: str, db_name: str):
        """Initialize the GoogleCloudSQLConfig with the provided parameters."""
        self.instance_connection_name = instance_connection_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
