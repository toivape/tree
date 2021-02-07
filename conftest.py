import pytest
import boto3
from moto import mock_s3
import os

TEST_REGION = 'us-east-1'

TEST_BUCKET = 'tree-upload'

TEST_OBJECT_NAME = 'tree-1000px.jpg'

TEST_FILE_PATH = 'test-data/tree-1000px.jpg'


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture(scope='function')
def s3(aws_credentials):
    with mock_s3():
        yield boto3.client('s3', region_name=TEST_REGION)


def create_test_bucket(s3):
    s3.create_bucket(Bucket=TEST_BUCKET)
    s3.upload_file(TEST_FILE_PATH, TEST_BUCKET, TEST_OBJECT_NAME)

