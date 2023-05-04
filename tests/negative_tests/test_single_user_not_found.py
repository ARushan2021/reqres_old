import allure
import pytest

from utils.site import ApiV1

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['150',
                          '155']
                         )
@allure.title('Неуспешный запрос информации о пользователе, неверный id')
def test_user_not_found(id_user):
    ApiV1().user_not_found(id_user)
