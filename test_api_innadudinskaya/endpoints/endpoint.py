import allure
import requests


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that name and data are the same as sent')
    def check_response_name_and_data_are_correct(self, name, color, size):
        assert self.json['name'] == name
        assert self.json['data']['color'] == color
        assert self.json['data']['size'] == size

    @allure.step('Check that name and size are the same as sent')
    def check_response_name_and_size_are_correct(self, name, size):
        assert self.json['name'] == name
        assert self.json['data']['size'] == size

    def last_element_id(self):
        init_response = requests.get(self.url)
        length = len(init_response.json()['data'])
        element_id = init_response.json()['data'][length - 1]['id']
        return element_id

    @allure.step('Check response code is 200')
    def check_response_status_code_is_correct(self, code=200):
        assert self.response.status_code == code

    @allure.step(f'Check that object id is correct')
    def check_object_id_is_correct(self, init_response, result_response):
        assert init_response.json()['id'] == result_response.json()['id']
        assert init_response.json()['data']['color'] == result_response.json()['data']['color']
        assert init_response.json()['data']['size'] == result_response.json()['data']['size']
        assert init_response.json()['name'] == result_response.json()['name']
