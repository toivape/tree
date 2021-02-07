from services import list_area_trees



def test_list_area_trees():
    area_trees = list_area_trees('aaf88678-6961-11eb-9439-0242ac130002')
    assert len(area_trees) == 20