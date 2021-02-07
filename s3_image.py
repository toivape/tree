from image_info import get_gps_info
import boto3
import uuid


# https://medium.com/@Christopher.Ryan/aws-lambda-s3-dynamodb-cli-948270d7515c
def _get_gps_info_s3(bucket_name, key):
    s3_client = boto3.client('s3')
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
    s3_client.download_file(bucket_name, key, download_path)
    return get_gps_info(download_path)


def _strore_gps_info(gps_info):
    """ Write GPS info to DynamoDB """
    pass


def store_image_info(bucket_name, key):
    # Get image gps info and store it to dynamodb
    gps_info = _get_gps_info_s3(bucket_name, key)
    _strore_gps_info(gps_info)














