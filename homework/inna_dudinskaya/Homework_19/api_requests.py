import requests


def post_an_object():
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
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.json())


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

    return response.json()['id']


def clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def put_an_object():
    object_id = new_object()
    body = {
        "data": {
            "color": "orange",
            "size": "small"
        },
        "name": "Inna test object1"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(f'http://objapi.course.qa-practice.com/object/{object_id}',
                            json=body,
                            headers=headers
                            ).json()
    assert response['name'] == 'Inna test object1'
    clear(object_id)


def patch_an_object():
    object_id = new_object()
    body = {
        "data": {
            "size": "large"
        },
        "name": "Inna test object1"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{object_id}',
                              json=body,
                              headers=headers
                              ).json()
    assert response['name'] == 'Inna test object1'
    clear(object_id)


def delete_an_object():
    object_id = new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    print(response)
    print(response.status_code)


post_an_object()
put_an_object()
patch_an_object()
delete_an_object()
