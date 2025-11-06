import requests
import pytest
import allure


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


@allure.feature('Objects')
@allure.story('Manipulate Objects')
@pytest.mark.critical
@pytest.mark.parametrize("object_name", [
    "Inna test object 1",
    "Inna test object 2",
    "Inna test object 3"
])
def test_post_an_object(object_name, text):
    with allure.step('Prepare test data'):
        body = {
            "data": {
                "color": "magenta",
                "size": "medium"
            },
            "name": object_name
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to create an object'):
        response = requests.post('http://objapi.course.qa-practice.com/object',
                                 json=body,
                                 headers=headers
                                 )
    with allure.step('Check response code is 200'):
        assert response.status_code == 200


@allure.feature('Objects')
@allure.story('Get an Object')
@pytest.mark.medium
def test_get_one_object(new_object_id):
    with allure.step(f'Run get request for object with id {new_object_id}'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object_id}').json()
    with allure.step(f'Check that object id is {new_object_id}'):
        assert response['id'] == new_object_id


@allure.feature('Objects')
@allure.story('Manipulate Objects')
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


@allure.feature('Objects')
@allure.story('Manipulate Objects')
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


@allure.feature('Objects')
@allure.story('Manipulate Objects')
@allure.title('Удаление объекта')
def test_delete_an_object(new_object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    print(response)
    assert response.status_code == 200, f"Delete failed: {response.text}"
