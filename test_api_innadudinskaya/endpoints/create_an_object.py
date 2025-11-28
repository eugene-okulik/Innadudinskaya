import requests
import allure

from test_api_innadudinskaya.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Create new Object')
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
