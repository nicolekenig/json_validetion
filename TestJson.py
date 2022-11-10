import json
import validetion as v


def read_json(json_data):
    with open(json_data) as json_file:
        data_file = json.load(json_file)
        people_dict = data_file['people'][0]
        families_dict = data_file['families'][0]
        # print(data_file)
        return people_dict, families_dict


def test_valid_person_id():
    for id in people_dict:
        # print(id)
        v.assert_string(id)
        v.assert_people_id(id)


def test_valid_person_name():
    for id in people_dict:
        name = people_dict[id]['name']
        v.assert_string(name)


def test_valid_person_surname():
    for id in people_dict:
        surname = people_dict[id]['surname']
        v.assert_string(surname)


def test_valid_person_age():
    for id in people_dict:
        age = people_dict[id]['age']
        v.assert_number(age)


def test_valid_person_family_member():
    for id in people_dict:
        surname = people_dict[id]['surname']
        name = people_dict[id]['name']
        family_member = people_dict[id]['family_member']
        v.assert_family_member_type(family_member)
        v.assert_person_is_in_family(person_name=name, person_surname=surname, person_family_member=family_member,
                                     families=families_dict)


def test_person_appears_once():
    v.assert_person_appears_once(people_dict)


def test_valid_family_id():
    for id in families_dict:
        v.assert_string(id)
        v.assert_family_id(id)


def test_valid_family_surname():
    for id in families_dict:
        v.assert_string(id)
        v.assert_unique_surname(family_id=id, family_surname=families_dict[id]['surname'], family_dict=families_dict)


def test_valid_family_has_kids():
    for id in families_dict:
        v.asser_boolean(families_dict[id]['has_kids'])
        v.assert_number(families_dict[id]["kids_num"])
        if families_dict[id]['has_kids']:
            v.assert_kid_num_more_then_zero(families_dict[id]["kids_num"])
            v.assert_list(families_dict[id]["kids"])
            v.assert_have_kids(families_dict[id]["kids"])
        else:
            v.assert_kid_num_is_zero(families_dict[id]["kids_num"])
            v.assert_have_no_kids(families_dict[id]["kids"])


def test_family_member_exists_in_person():
    for id in families_dict:
        surname = families_dict[id]["surname"]
        parents = families_dict[id]["parents"]
        kids = families_dict[id]["kids"]
        for parent in parents:
            v.assert_family_parent_in_people(surname=surname, name=parent, people=people_dict)
        if kids is not None:
            for kid in kids:
                v.assert_family_kid_in_people(surname=surname, name=kid, people=people_dict)

people_dict, families_dict = read_json('Task.json')


