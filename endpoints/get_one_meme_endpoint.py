import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetOneMeme(Endpoint):
    @allure.step('Получение одного мема')
    def get_one_meme(self, token, mem_id):
        self.response = requests.get(
            f'{self.url}/meme/{mem_id}',
            headers={'Authorization': token}
        )
        return self.response
