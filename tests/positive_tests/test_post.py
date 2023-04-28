import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, first_name',
                         [(f'{RESOURCE_USERS}', 'morpheus'),
                          (f'{RESOURCE_USERS}', 'QA engineer')]
                         )
@allure.title('Регистрируем нового пользователя')
def test_get_user(resource, first_name):
    endpoint_get = f'{BASE_URL}{resource}'
    APIRequests.create_new_user(endpoint_get, first_name)



# allure serve test_reports - формирование allure в html
# pip3 freeze > requarements.txt - обновлене файлика через терминал
