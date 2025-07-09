import requests
import allure
from endpoints.base_endpoint import Endpoint


class PutMeme(Endpoint):
    @allure.step('Обновление созданного мема')
    def put_meme(self, payload, mem_id, token):
        try:
            self.response = requests.put(
                f'{self.url}/meme/{mem_id}',
                json=payload,
                headers={'Authorization': token}
            )
            self.response.raise_for_status()
            self.json = self.response.json()
            return self.json
        except requests.exceptions.RequestException:
            print("Произошла ошибка")
            return self.response
