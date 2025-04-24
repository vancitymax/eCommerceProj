import os
from datetime import datetime

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

def pytest_configure(config):
    config._metadata['Project Name'] = 'OpenCart'
    config._metadata['Module name'] = 'Reg'
    config._metadata['Tester Name'] = 'Max'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("PYTHON_HOME",None)
    metadata.pop("Plugins",None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%Y%m%d-%H%M%S")+".html"