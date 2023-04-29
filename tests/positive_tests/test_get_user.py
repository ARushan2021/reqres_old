import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user',
                         [(f'{RESOURCE_USERS}', '2'),
                          (f'{RESOURCE_USERS}', '3')]
                         )
@allure.title('Получаем информацию об одном пользователе')
def test_get_user(resource, id_user):
    endpoint_get = f'{BASE_URL}{resource}{id_user}'
    APIRequests.get_request(endpoint_get, '200')

# allure serve test_reports - формирование allure в html
# pip3 freeze > requarements.txt - обновлене файлика через терминал
