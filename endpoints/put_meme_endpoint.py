import requests
import allure
from endpoints.base_endpoint import Endpoint


class PutMeme(Endpoint):
    @allure.step('Обновление созданного мема')
    def put_meme(self, payload, mem_id, token):
        self.response = requests.put(
            f'{self.url}/meme/{mem_id}',
            json=payload,
            headers={'Authorization': token}
        )
        return self.response
