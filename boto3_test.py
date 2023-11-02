"""
User migration from CSV to Digital Agency
"""
import boto3
import logging

logging.basicConfig(level=logging.DEBUG)

# Setup logging
logging.basicConfig(filename='api_requests.log', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.ERROR)


class S3Fetcher:
    def __init__(self, bucket, key, aws_access_key_id, aws_secret_access_key):
        self.bucket = bucket
        self.key = key
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def fetch_csv_data(self):
        try:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key
            )
            print('s3 path: ', self.bucket, self.key)
            obj = s3_client.get_object(Bucket=self.bucket, Key=self.key)
            csv_data = obj['Body'].read().decode('utf-8')
            return csv_data
        except Exception as e:
            logger.error(f"Error fetching data from S3 for key: {self.key}. Error: {e}")
            raise


def main():
    bucket = ''
    key = ''
    aws_access_key_id = ''
    aws_secret_access_key = ''

    s3_fetcher = S3Fetcher(bucket, key, aws_access_key_id, aws_secret_access_key)
    csv_data = s3_fetcher.fetch_csv_data()
    print('csv_data', csv_data)


if __name__ == '__main__':
    main()
