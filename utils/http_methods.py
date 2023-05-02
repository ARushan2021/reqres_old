import requests

from utils.logger import Logger

"""Список Http методов для тестирования 'https://reqres.in/'"""


class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookies = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, json):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, json):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result

    @staticmethod
    def patch(url, json):
        Logger.add_request(url, method="PATCH")
        result = requests.patch(url, json, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result
