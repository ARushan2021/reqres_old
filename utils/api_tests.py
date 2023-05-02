from utils.checking import Checking
from utils.http_methods import Http_methods

"""Методы для тестирования 'https://reqres.in/'"""


class APIRequests:
    @staticmethod
    def get_test(url, status_code, json_schema):
        get_result = Http_methods.get(url)
        Checking.check_all_status_code(get_result, status_code)
        Checking.validate_response_body(get_result, json_schema)
        Checking.validate_time_response(get_result)

    @staticmethod
    def post_test(url, body, status_code, json_schema):
        post_result = Http_methods.post(url, body)
        Checking.check_all_status_code(post_result, status_code)
        Checking.validate_response_body(post_result, json_schema)
        Checking.validate_time_response(post_result)

    @staticmethod
    def put_test(url, json, status_code, json_schema):
        put_result = Http_methods.put(url, json)
        Checking.check_all_status_code(put_result, status_code)
        Checking.validate_response_body(put_result, json_schema)
        Checking.validate_time_response(put_result)

    @staticmethod
    def patch_test(url, json, status_code, json_schema):
        patch_result = Http_methods.patch(url, json)
        Checking.check_all_status_code(patch_result, status_code)
        Checking.validate_response_body(patch_result, json_schema)
        Checking.validate_time_response(patch_result)

    @staticmethod
    def delete_test(url, status_code, json_schema):
        delete_result = Http_methods.delete(url)
        Checking.check_all_status_code(delete_result, status_code)
        Checking.validate_response_body(delete_result, json_schema)
        Checking.validate_time_response(delete_result)
