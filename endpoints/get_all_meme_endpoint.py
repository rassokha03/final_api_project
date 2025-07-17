import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetAllMeme(Endpoint):
    @allure.step('Получение всех мемов')
    def get_all_meme(self, token):
        try:
            self.response = requests.get(
                f'{self.url}/meme',
                headers={'Authorization': token}
            )
            self.response.raise_for_status()
            self.json = self.response.json()
            return self.json
        except requests.exceptions.RequestException:
            print("Произошла ошибка")
            return self.response

    @allure.step('Проверка, что в ответе вернулось не пустое значение')
    def check_emptiness(self):
        assert None not in self.json, 'Данные пустые'
