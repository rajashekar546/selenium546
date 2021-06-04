# Import the 'modules' that are required for execution for Selenium test automation

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture(params=["chrome", "firefox"])
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        #web_driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        #web_driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    request.cls.driver = web_driver

    yield
    web_driver.close()

@pytest.fixture
def app_url():
    url ="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    return url