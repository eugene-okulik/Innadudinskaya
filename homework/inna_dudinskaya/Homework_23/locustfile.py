from locust import task, HttpUser
import random


class ObjectUser(HttpUser):

    @task(3)
    def get_an_object(self):
        self.client.get(
            f'/object/{random.choice([1, 3137, 3142])}'
        )

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object'
        )
