
from dotenv import load_dotenv
load_dotenv()

import os
# print(os.environ)

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

from services_handle.logger.loggings import Logger

from services_handle.get_credentials import credentials