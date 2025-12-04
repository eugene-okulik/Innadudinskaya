import requests
import allure

from test_api_innadudinskaya.endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get an Object')
    def get_an_object(self, init_resp):
        try:
            element_id = init_resp.json()['id']
        except (ValueError, TypeError) as e:
            element_id = init_resp.json['id']
        self.response = requests.get(f'{self.url}/{element_id}')
        self.json = self.response.json()
