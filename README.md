#Проект по API тестированию reqres.ru

5 позитивных кейсов, по одноу запросу в каждом кейсе.
5 негативных кейсов, в 4-х по одному запросу и в одном два запроса.

Все кейсы валидируются на json-схему в body response (если в body пусто, значит проверяется, что пусто).
Некотрые поля в json-схеме проверяются на валидность значений.
Проверяется статус код.
Проверяется время response, должно быть не более 2-х сек.
Пишутся логи по всем запросам.
Формируется allure отчет.

# allure serve test_reports - формирование allure в html
# pytest tests/negative_tests/ -v -s --alluredir=./test_reports/
# pytest tests/positive_tests/ -v -s --alluredir=./test_reports/
# pytest tests/ --alluredir=./test_reports/
