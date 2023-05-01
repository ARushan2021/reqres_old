import allure
import pytest

from utils.api_steps import APIRequests
from configuration import *

"""Тестирование портала 'https://reqres.in/'"""


@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('resource, id_user',
                         [(f'{RESOURCE_REGISTER}', '150'),
                          (f'{RESOURCE_REGISTER}', '155')]
                         )
@allure.title('Не найден пользователь')
def test_user_not_found(resource, id_user):
    endpoint_post = f'{BASE_URL}{resource}{id_user}'
    APIRequests.get_test(endpoint_post, '404')



# allure serve test_reports - формирование allure в html
# pip3 freeze > requarements.txt - обновлене файлика через терминал
