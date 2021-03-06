# Import the 'modules' that are required for execution for Selenium test automation

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def driver_init(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(ChromeDriverManager().install())
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox()
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()


@pytest.mark.usefixtures("driver_init","app_url")
class BasicTest:
    pass

#@pytest.mark.parametrize("uname, upass, expresult", [("Admin", "admin123", "Dashboard"),("Admin1", "admin123", "Invalid credentials"),("", "admin123", "Username cannot be empty"),("Admin", "admin123", "Dashboard")])

@pytest.mark.parametrize("uname, upass", [("Admin", "admin123")])
class Test_OrangeHRM_Login(BasicTest):

    def test_open_url(self, uname, upass,app_url):
        # Step 2) Navigate to OrangeHRM
        #self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.get(app_url)
        # Step 3) Enter the Username & Enter Password
        username = self.driver.find_element_by_name("txtUsername")
        password = self.driver.find_element_by_name("txtPassword")
        submit = self.driver.find_element_by_name("Submit")
        username.send_keys(uname)
        password.send_keys(upass)
        # Step 4) Click Login
        submit.click()
        time.sleep(3)
        # Logout from application
        self.driver.find_element_by_id("welcome").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)