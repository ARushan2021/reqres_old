import allure
import pytest

from utils.site import ApiV1

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['20',
                          '31']
                         )
@allure.title('Удаление пользователя')
def test_delete_user(id_user):
    ApiV1().delete_user(number=id_user)
