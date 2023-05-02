import allure
import pytest

from configuration import BASE_URL, RESOURCE_USERS, REQUEST_BODY_POST, REQUEST_BODY_POST2
from schemas.empty_request_body import EmptyRequestBody
from utils.api_tests import APIRequests
from utils.http_methods import Http_methods

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, body',
                         [(f'{RESOURCE_USERS}', f'{REQUEST_BODY_POST}'),
                          (f'{RESOURCE_USERS}', f'{REQUEST_BODY_POST2}')]
                         )
@allure.title('Проверка информации о только что созданном пользователе')
def test_not_found_new_user(resource, body):
    endpoint_post = f'{BASE_URL}{resource}'
    # Создаем нового пользователя post-запрос, и вытаскиваем id
    response_body = Http_methods.post(endpoint_post, body).json()
    new_user_id = response_body['id']
    # Get-запрос с новым id
    endpoint_get = f'{BASE_URL}{resource}{new_user_id}'
    APIRequests.get_test(endpoint_get, '404', EmptyRequestBody.CURLY_BRACKETS)
