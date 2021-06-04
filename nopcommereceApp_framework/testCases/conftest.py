from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Fixtures are functions, which will run before each test function to which it is applied

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        #driver = webdriver.Chrome()
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        #driver = webdriver.Edge(executable_path="D:\\Selenium_Browser_Driver\\msedgedriver.exe")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver


def pytest_addoption(parser):  # This will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


########### PyTest HTML Report #############

def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Abhi Dixit'


############## It is hook for deleter/Modify Enviroment info to HTML Report####
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
