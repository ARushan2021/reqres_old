import allure
import pytest

from utils.site import ApiV1

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['2',
                          '3']
                         )
@allure.title('Получение информации о пользователе')
def test_single_user(id_user):
    ApiV1().check_users(number=id_user)
