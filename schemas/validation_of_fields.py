
class ValidationOfFields:
    """Валидация полей в json-схеме"""

    """Проверяем, что в заданном поле присутствует 'https://'"""
    @staticmethod
    def check_that_https_in_link(web_link):
        if 'https://' in web_link:
            return web_link
        else:
            raise ValueError(f'Не валидное поле: {web_link}')

    """Проверяем, что в заданном поле присутствует символ '@'"""
    @staticmethod
    def check_that_dog_presented_in_email_adress(email):
        if '@' in email:
            return email
        else:
            raise ValueError(f'Не валидное поле: {email}')
