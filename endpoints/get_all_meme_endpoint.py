import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetAllMeme(Endpoint):
    @allure.step('Получение всех мемов')
    def get_all_meme(self, token):
        self.response = requests.get(
            f'{self.url}/meme',
            headers={'Authorization': token}
        )
        return self.response
