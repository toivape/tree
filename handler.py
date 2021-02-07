import json
import logging
from services import list_areas
from services import list_area_trees


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def upload_img_s3_handler(event, context):
    print('S3 IMG CREATE OBJECT', event)   
    return {
        "status": 200,
        "message": "OK"
    }


def upload_image_service(event, context):
    print('UPLOADING EXIST', event)
    # Input params
    # Image data
    # Latitude
    # Longitude
    # Altitude
    # Timestamp
    # Uploader id
    # Return image id?

    return {
        "status": 200,
        "message": "OK"
    }    


def list_areas_service(event, context):
    areas = list_areas()
    return areas


def list_area_trees_service(event, context):
    """Return max 100 trees from one area"""
    area_id = event.get('areaId', 'aaf88678-6961-11eb-9439-0242ac130002')  # Dummy default uuid
    area_trees = list_area_trees(area_id)
    return area_trees


