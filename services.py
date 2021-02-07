

def _new_area(lat, lng, name, area_id):
    return {
        "latitude": lat,
        "longitude": lng,
        "name": name,
        "areaId": area_id
    }


DUMMY_AREAS = [
        _new_area(60.2398412, 24.8619622, 'Area #1', 'aaf88678-6961-11eb-9439-0242ac130002'),
        _new_area(62.1020064, 27.8574533, 'Area #2', 'aaf8898e-6961-11eb-9439-0242ac130002'),
        _new_area(62.5904329, 30.6187608, 'Area #3', 'aaf88b28-6961-11eb-9439-0242ac130002'),
        _new_area(62.1103215, 27.9495344, 'Area #4', 'aaf88cb8-6961-11eb-9439-0242ac130002'),
        _new_area(61.9330096, 25.4206923, 'Area #5', 'aaf88f10-6961-11eb-9439-0242ac130002'),
        _new_area(60.3127525, 23.9205989, 'Area #6', 'aaf890f0-6961-11eb-9439-0242ac130002'),
        _new_area(61.9696952, 22.8010617, 'Area #7', 'aaf893fc-6961-11eb-9439-0242ac130002'),
        _new_area(62.8448328, 24.9090951, 'Area #8', 'aaf89938-6961-11eb-9439-0242ac130002'),
        _new_area(63.6614721, 27.7390937, 'Area #9', 'aaf91516-6961-11eb-9439-0242ac130002')
    ]


def list_areas():
    return DUMMY_AREAS


def _new_tree(area, index):
    return {
        'latitude': area['latitude'] + (4*index) / 1000,
        'longitude': area['longitude'] + (4*index) / 1000,
        'description': "Tree #" + str(index),
        'treeId': '7d121cb0-6966-11eb-9439-0242ac130002',
        'treeLink': 'trees/7d121cb0-6966-11eb-9439-0242ac130002'
    }


def list_area_trees(area_id):
    area = [dummy for dummy in DUMMY_AREAS if dummy['areaId'] == area_id][0]
    return [_new_tree(area, x) for x in range(20)]
