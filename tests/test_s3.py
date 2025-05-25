from examples.S3 import s3_service
import os


def test_upload(bucket_name: str, file_name: str):
    s3_service.upload_file(file_name, bucket_name, file_name)
    file_info = s3_service.get_file(bucket_name, file_name)

    assert file_info.get("Body")


def test_download(bucket_name: str, file_name: str):
    s3_service.download_file(bucket_name, file_name, "check.png")

    assert os.path.exists("check.png")

    os.remove("check.png")


def test_delete(bucket_name: str, file_name: str):
    result = s3_service.delete_file(bucket_name, file_name)

    assert result.get("ResponseMetadata")
