import allure
import pytest

from utils.api_tests import APIRequests
from configuration import BASE_URL, RESOURCE_USERS
from schemas.empty_request_body import EmptyRequestBody

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user',
                         [(f'{RESOURCE_USERS}', '20'),
                          (f'{RESOURCE_USERS}', '31')]
                         )
@allure.title('Удаление пользователя')
def test_delete_user(resource, id_user):
    endpoint_delete = f'{BASE_URL}{resource}{id_user}'
    APIRequests.delete_test(endpoint_delete, '204', EmptyRequestBody.EMPTY_STR)

