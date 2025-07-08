import requests
import allure
from endpoints.base_endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Удаление мема')
    def delete_meme(self, meme_id, token):
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            headers={'Authorization': token}
        )
        return self.response
