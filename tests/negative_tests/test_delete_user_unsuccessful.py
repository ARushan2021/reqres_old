import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user, body',
                         [(f'{RESOURCE_USERS}', '100', f'{REQUEST_BODY_POST_NEGATIVE}'),
                          (f'{RESOURCE_USERS}', '310', f'{REQUEST_BODY_POST_NEGATIVE}')]
                         )
@allure.title('Удаляем пользователя неуспешно')
def test_delete_user(resource, id_user, body):
    endpoint_delete = f'{BASE_URL}{resource}{id_user}'
    APIRequests.delete_test(endpoint_delete, body, '400')

# allure serve test_reports - формирование allure в html
# pip3 freeze > requarements.txt - обновлене файлика через терминал
