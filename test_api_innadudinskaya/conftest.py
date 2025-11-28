import pytest
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
