import json

"""Методы для проверки ответов на запросы"""


class Checking:
    expected_status_code = 000
    number_of_response = 0
    lst_first_token = 'token'

    """Метод для проверки статус кода"""

    @staticmethod
    def check_all_status_code(response_result, expected_status_code):
        Checking.expected_status_code = expected_status_code
        assert response_result.status_code == int(Checking.expected_status_code), \
            f'Получен не верный статус код {response_result.status_code}'
        print(f' В ответе на запрос статус код верный - "{Checking.expected_status_code}"')

    # """Метод для проверки наличия обязательного поля"""
    #
    # @staticmethod
    # def check_json_token(response_result, expected_value):
    #     token = json.loads(response_result.text)
    #     lst_tokens = list(token)
    #     Checking.lst_first_token = lst_tokens[0]
    #     assert Checking.lst_first_token == expected_value, \
    #         f'Ошибка!!! в место поля "{expected_value}" указанно "{Checking.lst_first_token}"'
    #     print(f'В ответе на запрос присутствует обязательное поле - "{Checking.lst_first_token}"')

