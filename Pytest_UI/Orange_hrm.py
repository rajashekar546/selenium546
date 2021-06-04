import time
import pytest
#rom pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


#@pytest.mark.parametrize("uname, upass", [("Admin", "admin123"), ("Admin", "admin123")])
def test_list_valid_user():
    # from selenium import webdriver
    # from selenium.webdriver.common.action_chains import ActionChains
    # from time import sleep
    # # Step 1) Open Firefox
    from selenium.webdriver.common.keys import Keys
    # from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # get method to launch the URL
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    # identifying the source element
    source = driver.find_element_by_xpath("//span[text()='right click me']")
    # action chain object creation
    actionChains = ActionChains(driver)
    # right click operation and then perform
    actionChains.context_click(source).perform()
    driver.find_element_by_xpath("//span[text()='Copy']").click()
    time.sleep(5)
    ActTest = driver.switch_to.alert
    ActTest1 = ActTest.text
    print(ActTest1)
    ExpTest = "clicked: copy"
    assert ActTest1 == ExpTest
    ActTest.accept()
    # to close the browser
    driver.close()
