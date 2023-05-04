"""Методы для тестирования 'https://reqres.in/'"""

from utils.base_api_methods import Base_API_methods


class Request:
    """Твоя обертка для отправки запросов + логирование"""

    def get(self, url, status_code, json_schema):
        return Base_API_methods().request(method='GET', url=url, status_code=status_code, json_schema=json_schema)

    def post(self, url, body, status_code, json_schema):
        return Base_API_methods().request(method='POST', url=url, data=body, status_code=status_code,
                                          json_schema=json_schema)

    def put(self, url, body, status_code, json_schema):
        return Base_API_methods().request(method='PUT', url=url, data=body, status_code=status_code,
                                          json_schema=json_schema)

    def patch(self, url, body, status_code, json_schema):
        return Base_API_methods().request(method='PATCH', url=url, data=body, status_code=status_code,
                                          json_schema=json_schema)

    def delete(self, url, status_code, json_schema):
        return Base_API_methods().request(method='DELETE', url=url, status_code=status_code,
                                          json_schema=json_schema)

# class APIRequests:
#     @staticmethod
#     def get_test(url, status_code, json_schema):
#         get_result = Http_methods().request(method='GET', url=url)
#         Checking.checking_request(get_result, status_code, json_schema)
#         Logger.logging(response=get_result)
#
#     @staticmethod
#     def post_test(url, body, status_code, json_schema):
#         post_result = Http_methods().request(method='POST', url=url, data=body)
#         Checking.checking_request(post_result, status_code, json_schema)
#         Logger.logging(response=post_result)
#
#     @staticmethod
#     def put_test(url, body, status_code, json_schema):
#         put_result = Http_methods().request(method='PUT', url=url, data=body)
#         Checking.checking_request(put_result, status_code, json_schema)
#         Logger.logging(response=put_result)
#
#     @staticmethod
#     def patch_test(url, body, status_code, json_schema):
#         patch_result = Http_methods().request(method='PATCH', url=url, data=body)
#         Checking.checking_request(patch_result, status_code, json_schema)
#         Logger.logging(response=patch_result)
#
#     @staticmethod
#     def delete_test(url, status_code, json_schema):
#         delete_result = Http_methods().request(method='DELETE', url=url)
#         Checking.checking_request(delete_result, status_code, json_schema)
#         Logger.logging(response=delete_result)
