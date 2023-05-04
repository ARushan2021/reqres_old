import allure
import pytest

from utils.site import ApiV1

"""Тестирование портала 'https://reqres.in/'"""


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Негативное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user',
                         ['20',
                          '29']
                         )
@allure.title('Неуспешный запрос информации о пользователе, неверный resource')
def test_single_resource_not_found(id_user):
    ApiV1().single_resource_not_found(id_user)
