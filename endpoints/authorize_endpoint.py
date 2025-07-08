import requests
import allure
from endpoints.base_endpoint import Endpoint


class Authorize(Endpoint):

    @allure.step('Авторизация')
    def authorize(self, payload):
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=payload
        )
        return self.response

    @allure.step('Получение имени из ответа')
    def check_name_in_the_response(self, name):
        assert self.response.json()['user'] == name

    @allure.step('Проверка, что токен есть в ответе')
    def check_the_token_in_the_response(self):
        self.json = self.response.json()
        assert 'token' in self.json
