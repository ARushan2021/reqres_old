import allure
import pytest

from utils.api_tests import APIRequests
from configuration import BASE_URL, RESOURCE_REGISTER, REQUEST_BODY_POST, REQUEST_BODY_POST2
from schemas.post import PostUnseccessful

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, body',
                         [(f'{RESOURCE_REGISTER}', f'{REQUEST_BODY_POST}'),
                          (f'{RESOURCE_REGISTER}', f'{REQUEST_BODY_POST2}')]
                         )
@allure.title('Неуспешная регистрация нового пользователя')
def test_register_unsuccessful(resource, body):
    endpoint_post = f'{BASE_URL}{resource}'
    APIRequests.post_test(endpoint_post, body, '400', PostUnseccessful)

