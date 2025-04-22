import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default='chrome')
@pytest.fixture
def setup(request):
    browser = request.config.getoption('--browser')
    print(f"Running {browser}")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise TypeError(f"Browser {browser} is not supported")
    driver.maximize_window()
    yield driver
    driver.quit()
