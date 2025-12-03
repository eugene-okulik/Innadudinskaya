import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that name and data are the same as sent')
    def check_response_name_and_data_are_correct(self, body):
        assert self.json['name'] == body['name']
        assert self.json['data']['color'] == body['data']['color']
        assert self.json['data']['size'] == body['data']['size']

    @allure.step('Check that name and size are the same as sent')
    def check_response_name_and_size_are_correct(self, body):
        assert self.json['name'] == body['name']
        assert self.json['data']['size'] == body['data']['size']

    @allure.step('Check response code is 200')
    def check_response_status_code_is_correct(self, code=200):
        assert self.response.status_code == code

    @allure.step('Check that object id is correct')
    def check_object_id_is_correct(self, init_response):
        assert init_response.json()['id'] == self.json['id']
        assert init_response.json()['data']['color'] == self.json['data']['color']
        assert init_response.json()['data']['size'] == self.json['data']['size']
        assert init_response.json()['name'] == self.json['name']
