import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, body',
                         [(f'{RESOURCE_USERS}', f'{REQUEST_BODY_POST_NEGATIVE}'),
                          (f'{RESOURCE_USERS}', f'{REQUEST_BODY_POST_NEGATIVE2}')]
                         )
@allure.title('Неуспешное созадние нового пользователя')
def test_create_new_user_unseccessful(resource, body):
    endpoint_post = f'{BASE_URL}{resource}'
    APIRequests.post_test(endpoint_post, body, '400')
