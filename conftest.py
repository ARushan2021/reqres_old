import os

import pytest

"""Функция по очистке каталогов logs и reports"""


@pytest.fixture(scope='session')
def clear_test_reports_and_logs():
    folder_test_reports = 'test_reports/'
    for f in os.listdir(folder_test_reports):
        os.remove(os.path.join(folder_test_reports, f))

    folder_logs = 'logs/'
    for c in os.listdir(folder_logs):
        os.remove(os.path.join(folder_logs, c))
