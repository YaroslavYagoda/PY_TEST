import pytest


@pytest.fixture()
def enter_exit_positive():
    print('\nПсевдодействия до прогона теста positive')
    yield
    print('\nПсевдодействия после прогона теста')


@pytest.fixture()
def enter_exit_negative():
    print('\nПсевдодействия до прогона теста negative')
    yield
    print('\nПсевдодействия после прогона теста')


def test_send_mail_positive(enter_exit_negative):
    print('\nСообщение отправлено')


def test_send_mail_negative(enter_exit_positive):
    print('\nСообщение не отправлено')

