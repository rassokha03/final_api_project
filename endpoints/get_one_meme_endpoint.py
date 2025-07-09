import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetOneMeme(Endpoint):
    @allure.step('Получение одного мема')
    def get_one_meme(self, token, mem_id):
        try:
            self.response = requests.get(
                f'{self.url}/meme/{mem_id}',
                headers={'Authorization': token}
            )
            self.response.raise_for_status()
            self.json = self.response.json()
            return self.json
        except requests.exceptions.RequestException:
            print("Произошла ошибка")
            return self.response
