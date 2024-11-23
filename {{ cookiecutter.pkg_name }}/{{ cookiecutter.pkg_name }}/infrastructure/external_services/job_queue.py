from {{ cookiecutter.pkg_name }}.domain.interfaces import IDatabaseConnection, IJobQueue


class JobQueue(IJobQueue):
    """Class interacting with a job queue."""

    def __init__(self, db_connection: IDatabaseConnection, topic_path: str):
        """Initialize the JobQueue with a database connection and a Pub/Sub publisher.

        Args:
            db_connection (IDatabaseConnection): A connection to the database.
            topic_path (str): The path to the Pub/Sub topic where the jobs will be published.

        """
        self.connection = db_connection.get_connection()
        self.topic_path = topic_path

    async def enqueue_job(self, job_id: str, gcs_file_path: str) -> None:
        """Enqueues a job for processing by the job queue.

        Args:
            job_id (str): The ID of the job to enqueue.
            gcs_file_path (str): The file path in Google Cloud Storage where the job data is stored.

        """
        message_data = f"{job_id}:{gcs_file_path}".encode()
        future = self.connection.publish(self.topic_path, message_data)
        future.result(timeout=30)
