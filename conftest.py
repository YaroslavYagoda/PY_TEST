import pytest


# scope='function', разделение (изоляция) между тестами
@pytest.fixture()
def fixture_function():
    print('\nНачало фикстура (scope="function") (по умолчанию)')
    yield
    print('\nКонец фикстура (scope="function") (по умолчанию)')


# scope='module', разделение (изоляция) для модулей (данные едины для всех тестов одного модуля)
@pytest.fixture(scope='module')
def fixture_module():
    print('\nНачало фикстура (scope="module")')
    yield
    print('\nКонец фикстура (scope="module")')


# scope='package', глобально для всей папки (пакета)
@pytest.fixture(scope='package')
def fixture_package():
    print('\nНачало фикстура (scope="package")')
    yield
    print('\nКонец фикстура (scope="package")')

# scope='session', глобально для всех тестов во всех папках (не стал добавлять)
