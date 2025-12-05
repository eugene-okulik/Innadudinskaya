import requests
import allure

from test_api_innadudinskaya.endpoints.endpoint import Endpoint


class UpdateObjectPut(Endpoint):

    @allure.step('Update an Object Put')
    def make_changes_in_object_put(self, body, init_resp, headers=None):
        element_id = init_resp.json()['id']

        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{element_id}',
                                     json=body,
                                     headers=headers
                                     )
        self.json = self.response.json()
        return self.response
