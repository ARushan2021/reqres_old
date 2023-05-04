import allure
import pytest

from configuration import REQUEST_BODY_UPDATE, REQUEST_BODY_UPDATE2
from utils.site import ApiV1

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user, body',
                         [('8', f'{REQUEST_BODY_UPDATE}'),
                          ('9', f'{REQUEST_BODY_UPDATE2}')]
                         )
@allure.title('Частичное изменение параметров пользователя')
def test_partial_update_user(id_user, body):
    ApiV1().partial_update_user(number=id_user, body=body)
