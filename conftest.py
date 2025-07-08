#  добавить поулчение токена сюда??
import pytest



from endpoints.authorize_endpoint import Authorize
from endpoints.get_token_life_endpoint import Token
from endpoints.get_all_meme_endpoint import GetAllMeme
from endpoints.get_one_meme_endpoint import GetOneMeme
from endpoints.post_mem_endpoint import CreateMeme
from endpoints.put_meme_endpoint import PutMeme
from endpoints.delete_meme_endpoint import DeleteMeme


@pytest.fixture(scope='session')
def authorize_token_endpoint():
    return Authorize()


@pytest.fixture
def check_token_life_endpoint():
    return Token()


@pytest.fixture()
def get_all_meme():
    return GetAllMeme()


@pytest.fixture()
def get_one_meme():
    return GetOneMeme()


@pytest.fixture()
def create_new_meme():
    return CreateMeme()


@pytest.fixture()
def put_meme():
    return PutMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture(scope='session')
def create_token_for_test(authorize_token_endpoint):
    user = authorize_token_endpoint.authorize(payload={'name': 'Test User'})
    token = user.json()['token']
    return token


@pytest.fixture()
def get_name_from_token_for_test(create_token_for_test, check_token_life_endpoint):
    user = check_token_life_endpoint.check_token_life(create_token_for_test).text
    name = user.split('Username is ')[1]
    return name


@pytest.fixture()
def create_meme_for_test(create_token_for_test, create_new_meme, delete_meme):
    payload = {
        "text": "Meme for Test",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjdWb-f69SueqKnEmMVaF5O_WwsvW-9N91ww&s",
        "tags": ["cats", "pain"],
        "info": {
            "creator": "Andrey",
            "observer": "Eugene"
        }
    }
    mem_id = create_new_meme.create_mem(payload=payload, token=create_token_for_test).json()['id']
    yield mem_id
    delete_meme.delete_meme(meme_id=mem_id, token=create_token_for_test)
