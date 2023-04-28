import allure

from utils.http_methods import Http_methods
from utils.checking import Checking

"""Методы для тестирования 'The Star Wars API'"""


class APIRequests:
    @staticmethod
    def get_single_user(url):
        get_result = Http_methods.get(url)
        Checking.check_all_status_code(get_result, '200')

    @staticmethod
    def create_new_user(url, first_name):
        json = '{"first_name": "' + first_name + '"}'
        post_result = Http_methods.post(url, json)
        Checking.check_all_status_code(post_result, '201')

    @staticmethod
    def update_user(url, first_name):
        json = '{"first_name": "' + first_name + '"}'
        put_result = Http_methods.put(url, json)
        Checking.check_all_status_code(put_result, '200')

