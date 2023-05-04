import requests
from utils.logger import Logger
from utils.checking import Checking


"""Модуль содержит базовый метод для тестирования API"""


class Base_API_methods:

    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.cookies = ""

    def request(self, method: str, url: str, status_code: str, json_schema, data=None, headers=None, cookies=None)\
            -> requests.Response:
        headers = self.headers if headers is None else headers
        cookies = self.cookies if cookies is None else cookies
        response = requests.request(method=method, url=url, data=data, headers=headers, cookies=cookies)
        Logger.logging(response=response)
        Checking.checking_request(response, status_code, json_schema)

        return response












# class Http_methods:
#     headers = {'Content-Type': 'application/json'}
#     cookies = ""
#
#     @staticmethod
#     def get(url):
#         Logger.add_request(url, method="GET")
#         result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
#         Logger.add_response(result)
#         return result
#
#     @staticmethod
#     def post(url, json):
#         Logger.add_request(url, method="POST")
#         result = requests.post(url, json, headers=Http_methods.headers, cookies=Http_methods.cookies)
#         Logger.add_response(result)
#         return result
#
#     @staticmethod
#     def put(url, json):
#         Logger.add_request(url, method="PUT")
#         result = requests.put(url, json, headers=Http_methods.headers, cookies=Http_methods.cookies)
#         Logger.add_response(result)
#         return result
#
#     @staticmethod
#     def patch(url, json):
#         Logger.add_request(url, method="PATCH")
#         result = requests.patch(url, json, headers=Http_methods.headers, cookies=Http_methods.cookies)
#         Logger.add_response(result)
#         return result
#
#     @staticmethod
#     def delete(url):
#         Logger.add_request(url, method="DELETE")
#         result = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
#         Logger.add_response(result)
#         return result
