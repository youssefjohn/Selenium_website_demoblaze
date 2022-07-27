import pytest
from selenium import webdriver


@pytest.fixture(scope='class', autouse=True)
def setup(request, browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'ff':
        driver = webdriver.Firefox()
    elif browser.lower() == 'ie':
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome()

    print('Running Class level Setup')
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
    print("Running Class level Teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption("--browser")

























