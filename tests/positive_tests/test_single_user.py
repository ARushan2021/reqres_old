import allure
import pytest

from utils.api_tests import APIRequests
from configuration import BASE_URL, RESOURCE_USERS
from schemas.get import Get

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user',
                         [(f'{RESOURCE_USERS}', '2'),
                          (f'{RESOURCE_USERS}', '3')]
                         )
@allure.title('Получение информации о пользователе')
def test_single_user(resource, id_user):
    endpoint_get = f'{BASE_URL}{resource}{id_user}'
    APIRequests.get_test(endpoint_get, '200', Get)


