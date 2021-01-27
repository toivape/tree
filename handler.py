import json
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def upload_image(event, context):
    print('UPLOAD IMAGE EVENT', event)
   

    return {
        "status": 200,
        "message": "OK"
    }


