from pytest import fixture
import os


@fixture(scope="session", autouse=True)
def bucket_name() -> str:
    return os.environ.get("BUCKET_NAME", "littletestbucket1232")


@fixture(scope="session", autouse=True)
def file_name() -> str:
    return "example.png"
