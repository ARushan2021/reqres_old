import allure
import pytest

from utils.api_tests import APIRequests
from configuration import BASE_URL, RESOURCE_REGISTER
from schemas.empty_request_body import EmptyRequestBody

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user',
                         [(f'{RESOURCE_REGISTER}', '150'),
                          (f'{RESOURCE_REGISTER}', '155')]
                         )
@allure.title('Неуспешный запрос информации о пользователе, неверный id')
def test_user_not_found(resource, id_user):
    endpoint_post = f'{BASE_URL}{resource}{id_user}'
    APIRequests.get_test(endpoint_post, '404', EmptyRequestBody.CURLY_BRACKETS)

