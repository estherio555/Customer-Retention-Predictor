
class S3Handler:
    def __init__(self, logger: Logger, bucket_name: str):
        """
        Initializes the S3Handler with an S3 client and the specified bucket name.

        :param logger: Logger instance for logging S3 actions
        :param bucket_name: The name of the S3 bucket to interact with
        """
        creds = credentials()
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=creds.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=creds.AWS_SECRET_ACCESS_KEY,
            region_name=creds.AWS_REGION
        )
        self.bucket_name = bucket_name
        self.logger = logger.get_logger()

from services_handle.get_credentials import credentials