import requests
import allure
from endpoints.base_endpoint import Endpoint


class CreateMeme(Endpoint):
    @allure.step('Создание мема')
    def create_mem(self, payload, token):
        try:
            self.response = requests.post(
                f'{self.url}/meme',
                json=payload,
                headers={'Authorization': token}
            )
            self.response.raise_for_status()
            self.json = self.response.json()
            return self.json
        except requests.exceptions.RequestException:
            print("Произошла ошибка")
            return self.response
