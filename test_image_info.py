from image_info import get_gps_info


def test_get_gps_info():
    info = get_gps_info('test-data/tree-1000px.jpg')
    assert info['Latitude'] == 60.22808888888889
    assert info['Longitude'] == 24.85158888888889
    assert info['Altitude'] == 74.007
    assert info['Date'] == '01/27/2021'
