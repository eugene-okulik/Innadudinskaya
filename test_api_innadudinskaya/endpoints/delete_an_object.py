import requests
import allure

from test_api_innadudinskaya.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete an Object')
    def delete_an_object(self, init_resp):
        element_id = init_resp.json()['id']
        self.response = requests.delete(f'{self.url}/{element_id}')
        return self.response
