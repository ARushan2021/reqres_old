import allure
import pytest

from utils.api_tests import APIRequests
from configuration import BASE_URL, RESOURCE_NOT_FOUND
from schemas.empty_request_body import EmptyRequestBody

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user',
                         [(f'{RESOURCE_NOT_FOUND}', '20'),
                          (f'{RESOURCE_NOT_FOUND}', '29')]
                         )
@allure.title('Неуспешный запрос информации о пользователе, неверный resource')
def test_single_resource_not_found(resource, id_user):
    endpoint_patch = f'{BASE_URL}{resource}{id_user}'
    APIRequests.get_test(endpoint_patch, '404', EmptyRequestBody.CURLY_BRACKETS)


