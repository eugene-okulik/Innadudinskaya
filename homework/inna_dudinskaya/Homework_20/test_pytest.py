import requests
import pytest


@pytest.fixture(autouse=True)
def print_test_boundaries():
    print("\n=== before test ===")
    yield
    print("=== after test ===\n")


@pytest.fixture(scope='session')
def text():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def new_object_id():
    body = {
        "data": {
            "color": "magenta",
            "size": "medium"
        },
        "name": "Inna test object"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body,
                             headers=headers
                             )

    object_id = response.json()['id']
    print(object_id)
    yield object_id
    print('\ndeleting the object')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.mark.critical
@pytest.mark.parametrize("object_name", [
    "Inna test object 1",
    "Inna test object 2",
    "Inna test object 3"
])
def test_post_an_object(object_name, text):
    body = {
        "data": {
            "color": "magenta",
            "size": "medium"
        },
        "name": object_name
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body,
                             headers=headers
                             )
    assert response.status_code == 200


@pytest.mark.medium
def test_get_one_object(new_object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object_id}').json()
    assert response['id'] == new_object_id


def test_put_an_object(new_object_id):
    body = {
        "data": {
            "color": "orange",
            "size": "small"
        },
        "name": "Inna test object new"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_object_id}',
                            json=body,
                            headers=headers
                            ).json()
    assert response['name'] == 'Inna test object new'
    assert response['data']['color'] == 'orange'
    assert response['data']['size'] == 'small'


def test_patch_an_object(new_object_id):
    body = {
        "data": {
            "size": "large"
        },
        "name": "Inna test object new"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_object_id}',
                              json=body,
                              headers=headers
                              ).json()
    assert response['name'] == 'Inna test object new'
    assert response['data']['size'] == 'large'


def test_delete_an_object(new_object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    print(response)
    assert response.status_code == 200, f"Delete failed: {response.text}"
