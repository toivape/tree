from GPSPhoto import gpsphoto
import logging

# Requires all these to make gpshphoto to work:
# pip install gpsphoto
# pip install piexif
# pip install exifread
# pip install pillow

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_gps_info(path):
    """ Read image location from the file """
    logger.info(f'Opening image [{path}]')

    try:
        data = gpsphoto.getGPSData(path)
        result = {}
        for tag in data.keys():
            result[tag] = data[tag]

        print(result)
        return result

    except Exception as e:
        #logger.error(f'Failed to read location from image [{path}]', e)
        raise


def resize_image(path):
    pass
