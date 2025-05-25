from types_boto3_s3.type_defs import GetObjectOutputTypeDef, DeleteObjectOutputTypeDef

from examples.clients import s3_client
from typing import TypeVar
from types_boto3_s3 import S3Client


S3Bound = TypeVar("S3Bound", bound=S3Client)


class S3Service:
    def __init__(self, client: S3Bound):
        self._cl = client

    def upload_file(self, file_path: str, bucket: str, key: str) -> None:
        """Upload file to the s3 bucket"""
        self._cl.upload_file(file_path, bucket, key)

    def download_file(self, bucket: str, key: str, file_name: str) -> None:
        """Download the file from s3 bucket"""
        self._cl.download_file(bucket, key, file_name)

    def get_file(self, bucket: str, key: str) -> GetObjectOutputTypeDef:
        """Get file from bucket by key"""
        return self._cl.get_object(Bucket=bucket, Key=key)

    def delete_file(self, bucket: str, key: str) -> DeleteObjectOutputTypeDef:
        """Delete file from bucket"""
        return self._cl.delete_object(Bucket=bucket, Key=key)


s3_service = S3Service(s3_client)
