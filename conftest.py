"""Модуль содержит все декораторы проекта"""

import os

import pytest
from configuration import DIRECTORY_LOGS, DIRECTORY_TEST_REPORTS
from utils.site import Site


@pytest.fixture(scope='session')
def clear_test_reports_and_logs():
    """Декоратор по очистке каталогов logs и reports"""

    for f in os.listdir(DIRECTORY_TEST_REPORTS):
        os.remove(os.path.join(DIRECTORY_TEST_REPORTS, f))

    for c in os.listdir(DIRECTORY_LOGS):
        os.remove(os.path.join(DIRECTORY_LOGS, c))


@pytest.fixture(scope='session')
def base_api():
    """Декоратор"""
    return Site()
