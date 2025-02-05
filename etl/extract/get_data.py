from etl.utils.aws_manager import S3Buckets

def get_data(bucket_name, key):
    s3_conn = S3Buckets.credentials()