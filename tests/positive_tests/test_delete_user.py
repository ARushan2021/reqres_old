import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user, body',
                         [(f'{RESOURCE_USERS}', '20', ''),
                          (f'{RESOURCE_USERS}', '31', '')]
                         )
@allure.title('Удаляем пользователя')
def test_delete_user(resource, id_user, body):
    endpoint_delete = f'{BASE_URL}{resource}{id_user}'
    APIRequests.delete_test(endpoint_delete, body, '204')

# allure serve test_reports - формирование allure в html
# pip3 freeze > requarements.txt - обновлене файлика через терминал
