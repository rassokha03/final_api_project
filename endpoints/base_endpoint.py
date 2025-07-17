import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    authorization_payload = {'name': 'Test User'}
    response = None
    json = None

    @allure.step('Проверка на статус код 200')
    def check_status_code_200(self):
        assert self.response.status_code == 200, 'Status code is not 200'

    @allure.step('Проверка на статус код 400')
    def check_status_code_400(self):
        assert self.response.status_code == 400

    @allure.step('Проверка на статус код 404')
    def check_status_code_404(self):
        assert self.response.status_code == 404

    @allure.step('Проверка на статус код 401')
    def check_status_code_401(self):
        assert self.response.status_code == 401

    @allure.step('Проверка на то, кем был изменем мем')
    def check_who_updated_meme(self, name):
        assert self.response.json()["updated_by"] == name, 'Updated another meme'

    @allure.step('Проверка на статус код 403')
    def check_status_code_403(self):
        assert self.response.status_code == 403

    @allure.step('Сравнение тела запроса и ответа')
    def check_body_and_response(self, payload):
        assert self.response.json()["text"] == payload["text"]
        assert self.response.json()["url"] == payload["url"]
        assert self.response.json()["tags"] == payload["tags"]
        assert self.response.json()["info"] == payload["info"]
