import pytest
import allure
from data import (valid_data_from_test,
                  data_from_mest_with_messing_field,
                  valid_data_for_put)


@allure.feature('Авторизация')
@allure.story('Авторизация валидного пользователя')
@allure.title('Авторизация пользователя')
@allure.label('owner', 'Andrey Rassokhin')
def test_authorization_with_name(authorize_token_endpoint):
    payload = {
        'name': 'Test'
    }
    authorize_token_endpoint.authorize(payload=payload)
    authorize_token_endpoint.check_status_code_200()
    authorize_token_endpoint.check_name_in_the_response(name=payload['name'])
    authorize_token_endpoint.check_the_token_in_the_response()


@allure.feature('Авторизация')
@allure.story('Авторизация  не валидного пользователя')
@allure.title('Авторизация пользователя без имени')
@allure.label('owner', 'Andrey Rassokhin')
def test_authorization_with_empty_name(authorize_token_endpoint):
    payload = {
        'name': {}
    }
    authorize_token_endpoint.authorize(payload=payload)
    authorize_token_endpoint.check_status_code_400()


@allure.feature('Токен')
@allure.story('Проверка жизни  валидного токена')
@allure.title('Проверка жизни токена')
@allure.label('owner', 'Andrey Rassokhin')
def test_check_life_token(create_token_for_test, check_token_life_endpoint):
    check_token_life_endpoint.check_token_life(create_token_for_test)
    check_token_life_endpoint.check_status_code_200()
    check_token_life_endpoint.check_the_response_from_token()


@allure.feature('Токен')
@allure.story('Проверка жизни НЕ валидного токена')
@allure.title('Проверка токена с не валидными данными')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('token', ['', {}, None, 123456])
def test_check_token_is_alive_with_empty_token(check_token_life_endpoint, token):
    check_token_life_endpoint.check_token_life(token)
    check_token_life_endpoint.check_status_code_404()


@allure.feature('Мемы')
@allure.story('Get метод')
@allure.title('Получение всех мемов с валидным токеном')
@allure.label('owner', 'Andrey Rassokhin')
def test_get_all_meme(get_all_meme, create_token_for_test):
    get_all_meme.get_all_meme(create_token_for_test)
    get_all_meme.check_status_code_200()
    get_all_meme.check_emptiness()


@allure.feature('Мемы')
@allure.story('Get метод')
@allure.title('Получение всех мемов с не валидным токеном')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('token', [None, 'badToKeN'])
def test_get_all_meme_with_bad_token(get_all_meme, token):
    get_all_meme.get_all_meme(token)
    get_all_meme.check_status_code_401()


@allure.feature('Мемы')
@allure.story('Get метод')
@allure.title('Получение одного мема с валидным токеном')
@allure.label('owner', 'Andrey Rassokhin')
def test_get_one_meme(get_one_meme, create_token_for_test):
    get_one_meme.get_one_meme(create_token_for_test, mem_id=1)
    get_one_meme.check_status_code_200()
    get_one_meme.check_mem_id(mem_id=1)


@allure.feature('Мемы')
@allure.story('Get метод')
@allure.title('Получение не существующего мема')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('mem_id', ['', 123123123, 'Newmeme'])
def test_get_a_non_existent_meme(create_token_for_test, get_one_meme, mem_id):
    get_one_meme.get_one_meme(create_token_for_test, mem_id=mem_id)
    get_one_meme.check_status_code_404()


@allure.feature('Мемы')
@allure.story('Post метод')
@allure.title('Создание нового мема с валидным токеном')
@allure.label('owner', 'Andrey Rassokhin')
def test_create_new_meme(create_token_for_test, create_new_meme, get_name_from_token_for_test):
    payload = valid_data_from_test()
    create_new_meme.create_mem(token=create_token_for_test, payload=payload)
    create_new_meme.check_status_code_200()
    create_new_meme.check_body_and_response(payload=valid_data_from_test())
    create_new_meme.check_who_updated_meme(get_name_from_token_for_test)


@allure.feature('Мемы')
@allure.story('Post метод')
@allure.title('Создание нового мема с пустыми обязательными полями')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('field', ['text', 'url', 'tags', 'info'])
def test_with_missing_field(create_token_for_test, create_new_meme, field):
    payload = data_from_mest_with_messing_field(field)
    create_new_meme.create_mem(token=create_token_for_test, payload=payload)
    create_new_meme.check_status_code_400()


@allure.feature('Мемы')
@allure.story('Post метод')
@allure.title('Создание нового мема с  НЕ валидным токеном')
@allure.label('owner', 'Andrey Rassokhin')
def test_create_meme_with_bad_token(create_new_meme):
    payload = valid_data_from_test()
    create_new_meme.create_mem(token='badTokEn', payload=payload)
    create_new_meme.check_status_code_401()


@allure.feature('Мемы')
@allure.story('Post метод')
@allure.title('Создание нового мема с не подходящим форматом текста')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('bad_format_text', [1321, ['test'], {'test': 'test'}])
def test_create_meme_with_bad_format_text(create_token_for_test, create_new_meme, bad_format_text):
    payload = valid_data_from_test()
    payload['text'] = bad_format_text
    create_new_meme.create_mem(token=create_token_for_test, payload=payload)
    create_new_meme.check_status_code_400()


@allure.feature('Мемы')
@allure.story('Post метод')
@allure.title('Создание нового мема с не подходящим форматом информации')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('bad_format_info', ['test', 123, ['test']])
def test_create_meme_with_bad_format_info(create_token_for_test, create_new_meme, bad_format_info):
    payload = valid_data_from_test()
    payload['info'] = bad_format_info
    create_new_meme.create_mem(token=create_token_for_test, payload=payload)
    create_new_meme.check_status_code_400()


@allure.feature('Мемы')
@allure.story('Post метод')
@allure.title('Создание нового мема с не подходящим форматом тегов')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('bad_format_tags', ['test', 123, {'test': 'test'}, None])
def test_create_meme_with_bad_format_tags(create_token_for_test, create_new_meme, bad_format_tags):
    payload = valid_data_from_test()
    payload['tags'] = bad_format_tags
    create_new_meme.create_mem(token=create_token_for_test, payload=payload)
    create_new_meme.check_status_code_400()


@allure.feature('Мемы')
@allure.story('Post метод')
@allure.title('Создание нового мема с пустым УРЛом')
@allure.label('owner', 'Andrey Rassokhin')
def test_create_meme_with_bad_url(create_token_for_test, create_new_meme):
    payload = valid_data_from_test()
    payload['url'] = None
    create_new_meme.create_mem(token=create_token_for_test, payload=payload)
    create_new_meme.check_status_code_400()


@allure.feature('Мемы')
@allure.story('Delete метод')
@allure.title('Удаление мема')
@allure.label('owner', 'Andrey Rassokhin')
def test_delete_meme(create_meme_for_test, create_token_for_test, delete_meme, get_one_meme):
    mem_id = create_meme_for_test
    delete_meme.delete_meme(meme_id=mem_id, token=create_token_for_test)
    delete_meme.check_status_code_200()
    get_one_meme.get_one_meme(token=create_token_for_test, mem_id=mem_id)
    get_one_meme.check_status_code_404()


@allure.feature('Мемы')
@allure.story('Delete метод')
@allure.title('Удаление НЕ существующего мема')
@allure.label('owner', 'Andrey Rassokhin')
def test_delete_meme_not_existent(delete_meme, create_token_for_test):
    delete_meme.delete_meme(meme_id=9999, token=create_token_for_test)
    delete_meme.check_status_code_404()


@allure.feature('Мемы')
@allure.story('Delete метод')
@allure.title('Удаление мема, созданного другим ползователем')
@allure.label('owner', 'Andrey Rassokhin')
def test_delete_meme_another_creator(delete_meme, create_token_for_test):
    delete_meme.delete_meme(meme_id=1, token=create_token_for_test)
    delete_meme.check_status_code_403()


@allure.feature('Мемы')
@allure.story('Put метод')
@allure.title('Обновление мема ')
@allure.label('owner', 'Andrey Rassokhin')
def test_put_meme_with_valid_data(create_meme_for_test, put_meme, get_name_from_token_for_test, create_token_for_test, get_one_meme):
    payload_for_put = valid_data_for_put(mem_id=create_meme_for_test)
    put_meme.put_meme(payload_for_put, mem_id=create_meme_for_test, token=create_token_for_test)
    put_meme.check_status_code_200()
    put_meme.check_who_updated_meme(name=get_name_from_token_for_test)
    put_meme.check_body_and_response(payload=payload_for_put)


@allure.feature('Мемы')
@allure.story('Put метод')
@allure.title('Обновление мема с не подходящим форматом текста')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('bad_format_text', [1321, ['test'], {'test': 'test'}])
def test_put_meme_with_bad_format_text(create_meme_for_test, put_meme, create_token_for_test, bad_format_text):
    payload_for_put = valid_data_for_put(mem_id=create_meme_for_test)
    payload_for_put['text'] = bad_format_text
    put_meme.put_meme(payload=payload_for_put, mem_id=create_meme_for_test, token=create_token_for_test)
    put_meme.check_status_code_400()


@allure.feature('Мемы')
@allure.story('Put метод')
@allure.title('Обновление мема с не подходящим форматом информации')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('bad_format_info', ['test', 123, ['test']])
def test_put_meme_with_bad_format_info(create_meme_for_test, put_meme, create_token_for_test, bad_format_info):
    payload_for_put = valid_data_for_put(mem_id=create_meme_for_test)
    payload_for_put['info'] = bad_format_info
    put_meme.put_meme(payload=payload_for_put, mem_id=create_meme_for_test, token=create_token_for_test)
    put_meme.check_status_code_400()


@allure.feature('Мемы')
@allure.story('Put метод')
@allure.title('Обновление мема с не подходящим форматом тегов')
@allure.label('owner', 'Andrey Rassokhin')
@pytest.mark.parametrize('bad_format_tags', ['test', 123, {'test': 'test'}, None])
def test_put_meme_with_bad_format_tags(create_meme_for_test, put_meme, create_token_for_test, bad_format_tags):
    payload_for_put = valid_data_for_put(mem_id=create_meme_for_test)
    payload_for_put['tags'] = bad_format_tags
    put_meme.put_meme(payload=payload_for_put, mem_id=create_meme_for_test, token=create_token_for_test)
    put_meme.check_status_code_400()
