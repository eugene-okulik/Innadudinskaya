import pytest
import allure

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


@pytest.fixture()
def new_object(create_object_endpoint, delete_object_endpoint):
    body = {
        "data": {
            "color": "magenta",
            "size": "medium"
        },
        "name": "Inna test object"
    }
    response = create_object_endpoint.create_new_object(body)
    object_id = response.json()['id']
    with allure.step('Test object creation'):
        print(f"Created object with ID: {object_id}")

    yield response

    with allure.step('Test object deletion'):
        delete_object_endpoint.delete_an_object(response)
        print(f'\nDeleting object with ID: {object_id}')
