import pytest

TEST_DATA = [
    {'data': {'color': 'magenta', 'size': 'medium'},
     'name': 'Inna test object 1'
     },
    {'data': {'color': 'magenta', 'size': 'medium'},
     'name': 'Inna test object 2'
     },
    {'data': {'color': 'magenta', 'size': 'medium'},
     'name': 'Inna test object 3'
     }
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_an_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(body=data)
    create_object_endpoint.check_response_status_code_is_correct()


@pytest.mark.parametrize('data', TEST_DATA)
def test_get_one_object(get_object_endpoint, create_object_endpoint, data):
    init_response = create_object_endpoint.create_new_object(body=data)
    element_id = init_response.json()['id']
    result_response = get_object_endpoint.get_an_object(element_id)
    get_object_endpoint.check_object_id_is_correct(init_response, result_response)


def test_put_an_object(update_object_endpoint_put):
    body = {
        "data": {
            "color": "orange",
            "size": "small"
        },
        "name": "Inna test object new"
    }
    update_object_endpoint_put.make_changes_in_object_put(body)
    update_object_endpoint_put.check_response_status_code_is_correct()
    update_object_endpoint_put.check_response_name_and_data_are_correct(body['name'], body['data']['color'],
                                                                        body['data']['size'])


def test_patch_an_object(update_object_endpoint_patch):
    body = {
        "data": {
            "size": "large"
        },
        "name": "Inna test object new111"
    }
    update_object_endpoint_patch.make_changes_in_object_patch(body)
    update_object_endpoint_patch.check_response_status_code_is_correct()
    update_object_endpoint_patch.check_response_name_and_size_are_correct(body['name'], body['data']['size'])


@pytest.mark.parametrize('data', TEST_DATA)
def test_delete_an_object(delete_object_endpoint, create_object_endpoint, get_object_endpoint, data):
    init_response = create_object_endpoint.create_new_object(body=data)
    element_id = init_response.json()['id']
    delete_object_endpoint.delete_an_object(element_id)
    delete_object_endpoint.check_response_status_code_is_correct()
    get_object_endpoint.get_an_object(element_id)
    get_object_endpoint.check_response_status_code_is_correct(code=404)
