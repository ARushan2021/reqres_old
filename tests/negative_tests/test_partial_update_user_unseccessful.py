import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user, body',
                         [(f'{RESOURCE_USERS}', '8', f'{REQUEST_BODY_POST_NEGATIVE}'),
                          (f'{RESOURCE_USERS}', '9', f'{REQUEST_BODY_POST_NEGATIVE2}')]
                         )
@allure.title('Частично изменяем параметры пользователя неуспешно')
def test_partial_update_user_unseccessful(resource, id_user, body):
    endpoint_patch = f'{BASE_URL}{resource}{id_user}'
    APIRequests.patch_test(endpoint_patch, body, '400')
