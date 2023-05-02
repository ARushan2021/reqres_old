import allure
import pytest

from utils.api_tests import APIRequests
from configuration import BASE_URL, RESOURCE_USERS, REQUEST_BODY_UPDATE, REQUEST_BODY_UPDATE2
from schemas.put_patch import PutPatch

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user, body',
                         [(f'{RESOURCE_USERS}', '6', f'{REQUEST_BODY_UPDATE}'),
                          (f'{RESOURCE_USERS}', '7', f'{REQUEST_BODY_UPDATE2}')]
                         )
@allure.title('Изменение всех параметров пользователя')
def test_update_user(resource, id_user, body):
    endpoint_put = f'{BASE_URL}{resource}{id_user}'
    APIRequests.put_test(endpoint_put, body, '200', PutPatch)
