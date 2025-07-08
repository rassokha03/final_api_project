import requests
import allure
from endpoints.base_endpoint import Endpoint


class CreateMeme(Endpoint):
    @allure.step('Создание мема')
    def create_mem(self, payload, token):
        self.response = requests.post(
            f'{self.url}/meme',
            json=payload,
            headers={'Authorization': token}
        )
        return self.response

    @allure.step('Сравнение созданного тела и ответа созданного мема')
    def check_body_and_response(self, payload):
        assert self.response.json()["text"] == payload["text"]
        assert self.response.json()["url"] == payload["url"]
        assert self.response.json()["tags"] == payload["tags"]
        assert self.response.json()["info"] == payload["info"]
