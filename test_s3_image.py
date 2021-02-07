from s3_image import _get_gps_info_s3
from conftest import create_test_bucket


def test_get_gps_info(s3):
    create_test_bucket(s3)
    info = _get_gps_info_s3('tree-upload', 'tree-1000px.jpg')
    assert info['Latitude'] == 60.22808888888889
    assert info['Longitude'] == 24.85158888888889
    assert info['Altitude'] == 74.007
    assert info['Date'] == '01/27/2021'





