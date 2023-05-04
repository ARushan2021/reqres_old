import allure
import pytest

from configuration import REQUEST_BODY_POST, REQUEST_BODY_POST2
from utils.site import ApiV1

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('body',
                         [f'{REQUEST_BODY_POST}',
                          f'{REQUEST_BODY_POST2}']
                         )
@allure.title('Проверка информации о только что созданном пользователе')
def test_not_found_new_user(body):
    ApiV1().not_found_new_user(body=body)
