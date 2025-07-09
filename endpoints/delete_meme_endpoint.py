import requests
import allure
from endpoints.base_endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Удаление мема')
    def delete_meme(self, meme_id, token):
        try:
            self.response = requests.delete(
                f'{self.url}/meme/{meme_id}',
                headers={'Authorization': token}
            )
            self.response.raise_for_status()
            self.json = self.response.json()
            return self.json
        except requests.exceptions.RequestException:
            print("Произошла ошибка")
            return self.response
