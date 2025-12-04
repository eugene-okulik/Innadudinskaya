import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that name and data are the same as sent')
    def check_response_name_and_data(self, body):
        assert self.json['name'] == body['name']
        assert self.json['data']['color'] == body['data']['color']
        assert self.json['data']['size'] == body['data']['size']

    @allure.step('Check that name and size are changed')
    def check_response_name_changed(self, body):
        assert self.json['name'] == body['name']

    @allure.step('Check that color is not changed')
    def check_response_fields_not_changed(self, init_object, changed_object):
        assert init_object.json()['data']['color'] == changed_object.json['data']['color']
        assert init_object.json()['data']['size'] == changed_object.json['data']['size']

    @allure.step('Check response code is 200')
    def check_response_status_code_is_correct(self, code=200):
        assert self.response.status_code == code

    @allure.step('Check that object id is correct')
    def check_object_id_data(self, init_response):
        assert init_response.json()['data']['color'] == self.json['data']['color']
        assert init_response.json()['data']['size'] == self.json['data']['size']
        assert init_response.json()['name'] == self.json['name']
