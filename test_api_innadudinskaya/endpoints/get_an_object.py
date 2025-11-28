import requests
import allure

from test_api_innadudinskaya.endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get an Object')
    def get_an_object(self, element_id):
        self.response = requests.get(f'{self.url}/{element_id}')
        self.json = self.response.json() if self.response.status_code == 200 else None
        return self.response
