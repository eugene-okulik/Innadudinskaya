import pytest
import requests

from test_api_innadudinskaya.endpoints.create_an_object import CreateObject
from test_api_innadudinskaya.endpoints.get_an_object import GetObject
from test_api_innadudinskaya.endpoints.update_an_object_put import UpdateObjectPut
from test_api_innadudinskaya.endpoints.update_an_object_patch import UpdateObjectPatch
from test_api_innadudinskaya.endpoints.delete_an_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint_put():
    return UpdateObjectPut()


@pytest.fixture()
def update_object_endpoint_patch():
    return UpdateObjectPatch()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture(scope="session")
def new_object():
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
    print(f"Created object with ID: {object_id}")
    yield response
    print(f'\nDeleting object with ID: {object_id}')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
