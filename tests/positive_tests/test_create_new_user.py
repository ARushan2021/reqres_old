import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, body',
                         [(f'{RESOURCE_USERS}', f'{REQUEST_BODY_POST}'),
                          (f'{RESOURCE_USERS}', f'{REQUEST_BODY_POST2}')]
                         )
@allure.title('Регистрируем нового пользователя')
def test_create_new_user(resource, body):
    endpoint_post = f'{BASE_URL}{resource}'
    APIRequests.post_test(endpoint_post, body, '201')



# allure serve test_reports - формирование allure в html
# pip3 freeze > requarements.txt - обновлене файлика через терминал
