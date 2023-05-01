import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user, body',
                         [(f'{RESOURCE_USERS}', '8', f'{REQUEST_BODY_UPDATE}'),
                          (f'{RESOURCE_USERS}', '9', f'{REQUEST_BODY_UPDATE2}')]
                         )
@allure.title('Частично изменяем все параметры пользователя')
def test_partial_update_user(resource, id_user, body):
    endpoint_patch = f'{BASE_URL}{resource}{id_user}'
    APIRequests.patch_test(endpoint_patch, body, '200')
