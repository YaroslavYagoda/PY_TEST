import pytest


@pytest.fixture()
def before_start():
    print('\nПсевдодействия до прогона теста')


def test_send_mail_positive(before_start):
    print('\nСообщение отправлено')


def test_send_mail_negative(before_start):
    print('\nСообщение не отправлено')
