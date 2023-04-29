import allure

from utils.http_methods import Http_methods
from utils.checking import Checking

"""Методы для тестирования 'https://reqres.in/'"""


class APIRequests:
    @staticmethod
    def get_request(url, status_code):
        get_result = Http_methods.get(url)
        Checking.check_all_status_code(get_result, status_code)

    @staticmethod
    def post_request(url, body, status_code):
        post_result = Http_methods.post(url, body)
        Checking.check_all_status_code(post_result, status_code)

    @staticmethod
    def put_request(url, json, status_code):
        put_result = Http_methods.put(url, json)
        Checking.check_all_status_code(put_result, status_code)

    @staticmethod
    def patch_request(url, json, status_code):
        patch_result = Http_methods.patch(url, json)
        Checking.check_all_status_code(patch_result, status_code)

    @staticmethod
    def delete_request(url, status_code):
        delete_result = Http_methods.delete(url)
        print(status_code)
        Checking.check_all_status_code(delete_result, status_code)