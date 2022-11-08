def assert_number(num):
    assert type(num) is int


def assert_string(string):
    assert type(string) is str


def assert_list(arr):
    assert type(arr) is list


def asser_boolean(boolean):
    assert type(boolean) is bool


def assert_family_member_type(family_member):
    flag = False
    if family_member == 'kid' or family_member == 'parent':
        flag = True
    assert flag is True


def assert_people_id(id):
    assert len(id) is 5


def assert_family_id(id):
    id_as_list = list(id)
    flag = False
    if id_as_list[0] is '9' and id_as_list[1] is '9' and id_as_list[2] is '9' and id_as_list[3] is '-' and len(
            id_as_list[4:]) is 4:
        flag = True
    assert flag is True


def assert_unique_surname(family_id, family_surname, family_dict):
    for id in family_dict:
        if id is not family_id:
            assert family_dict[id]['surname'] is not family_surname


def assert_person_is_in_family(person_name, person_surname, person_family_member, families):
    for family_id in families:
        if families[family_id]['surname'] is person_surname:
            assert person_name in families[family_id][person_family_member]


def assert_person_appears_once(people_dict):
    # check that the same person (by surename and name) isn't write twice in people in a different id
    for person_id_1 in people_dict:
        for person_id_2 in people_dict:
            if person_id_2 is not person_id_1:
                assert (people_dict[person_id_1]['surname'] is not people_dict[person_id_2]['surname']) and (
                        people_dict[person_id_1]['name'] is not people_dict[person_id_1]['name'])


def assert_kid_num_more_then_zero(kids_num):
    assert kids_num > 0


def assert_have_kids(kids):
    assert len(kids) > 0


def assert_kid_num_is_zero(kids_num):
    assert kids_num is 0


def assert_have_no_kids(kids):
    assert kids is None


def assert_family_parent_in_people(surname, name, people):
    is_exists = False
    for id in people:
        if people[id]["surname"] is surname and people[id]["name"] is name and people[id]["family_member"] is "parent":
            is_exists = True
    assert is_exists is True


def assert_family_kid_in_people(surname, name, people):
    is_exists = False
    for id in people:
        if people[id]["surname"] is surname and people[id]["name"] is name and people[id]["family_member"] is "kid":
            is_exists = True
    assert is_exists is True
