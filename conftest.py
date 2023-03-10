import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as Options_Firefox


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='en-gb')
    parser.addoption("--browser_name", action="store", default='firefox',
                     help="Choose: chrome or firefox")


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = Options_Firefox()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
