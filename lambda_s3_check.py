"""
lambda S3
"""
import boto3

# ACCESS_KEY SECRET_KEY
ACCESS_KEY = ""
SECRET_KEY = ""

s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)


def main() -> None:
    """main"""
    try:
        response = s3_client.get_object(Bucket="youbora-content-watched", Key='Report1.csv.gz')
        print('response', response)
    except Exception as e:
        print("ERROR:", e)
        raise e

    print('result')


if __name__ == "__main__":
    main()
