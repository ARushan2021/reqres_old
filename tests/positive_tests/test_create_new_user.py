import allure
import pytest

from utils.api_tests import APIRequests
from configuration import BASE_URL, RESOURCE_USERS, REQUEST_BODY_POST, REQUEST_BODY_POST2
from schemas.post import Post

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, body',
                         [(f'{RESOURCE_USERS}', f'{REQUEST_BODY_POST}'),
                          (f'{RESOURCE_USERS}', f'{REQUEST_BODY_POST2}')]
                         )
@allure.title('Регистрация нового пользователя')
def test_create_new_user(resource, body):
    endpoint_post = f'{BASE_URL}{resource}'
    APIRequests.post_test(endpoint_post, body, '201', Post)

