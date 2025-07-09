import requests
import allure
from endpoints.base_endpoint import Endpoint


class Token(Endpoint):
    @allure.step('Проверка на жизнь токена')
    def check_token_life(self, token):
        try:
            self.response = requests.get(
                f'{self.url}/authorize/{token}'
            )
            self.response.raise_for_status()
            self.json = self.response.text
            return self.json
        except requests.exceptions.RequestException:
            print("Произошла ошибка")
            return self.response

    @allure.step('Проверка на то, что токен жив')
    def check_the_response_from_token(self):
        assert 'Token is alive.' in self.json, 'Token expired'
