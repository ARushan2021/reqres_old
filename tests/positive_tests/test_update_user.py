import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user, body',
                         [(f'{RESOURCE_USERS}', '6', f'{REQUEST_BODY_UPDATE}'),
                          (f'{RESOURCE_USERS}', '7', f'{REQUEST_BODY_UPDATE2}')]
                         )
@allure.title('Изменяем все параметры пользователя')
def test_update_user(resource, id_user, body):
    endpoint_put = f'{BASE_URL}{resource}{id_user}'
    APIRequests.put_test(endpoint_put, body, '200')
