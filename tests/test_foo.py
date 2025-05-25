import boto3
import os

BUCKET_NAME = os.environ.get('BUCKET_NAME')

def test_something():
    client = boto3.client("s3")
    assert isinstance(client.list_objects(Bucket=BUCKET_NAME), dict)