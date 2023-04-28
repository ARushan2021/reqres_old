import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user, first_name',
                         [(f'{RESOURCE_USERS}', '6', 'morp'),
                          (f'{RESOURCE_USERS}', '7', 'Automatic QA engineer')]
                         )
@allure.title('Изменяем все параметры пользователя')
def test_put_user(resource, id_user, first_name):
    endpoint_get = f'{BASE_URL}{resource}{id_user}'
    APIRequests.update_user(endpoint_get, first_name)
