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
@allure.title('Не успешный вход в систему')
def test_login_unsuccessful(body):
    ApiV1().login_unsuccessful(body)
