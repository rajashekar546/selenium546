import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select



#browser = webdriver.Firefox(executable_path='C:\\Users\\admin\\PycharmProjects\\Python-selenium\\Browser_Driver\\geckodriver.exe')
#browser = webdriver.Chrome(executable_path="C:\\Users\\admin\\PycharmProjects\\Python-selenium\\Browser_Driver\\chromedriver.exe")
browser = webdriver.Chrome(ChromeDriverManager().install())
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#browser = webdriver.Edge(EdgeChromiumDriverManager().install())

browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
username =browser.find_element_by_xpath("//input[@id='txtUsername']")
password =browser.find_element_by_xpath("//input[@id='txtPassword']")
login = browser.find_element_by_xpath("//input[@id='btnLogin']")
username.send_keys("Admin")
password.send_keys("admin123")
login.click()
wait = WebDriverWait(browser,20)
page_title =browser.title
assert page_title == "OrangeHRM"
Admin_menu =browser.find_element_by_xpath("//b[normalize-space()='Admin']")
action=ActionChains(browser)
action.move_to_element(Admin_menu).perform()
user_mgmt =browser.find_element_by_xpath("//a[normalize-space()='User Management']")
action.move_to_element(user_mgmt).perform()
users =browser.find_element_by_xpath("//a[normalize-space()='Users']")
action.move_to_element(users).perform()
users.click()
time.sleep(5)
status = Select(browser.find_element_by_id("searchSystemUser_status"))
status_values = status.options
list1 =[]
for index in range(len(status_values)):
    list = status_values[index].text

    list1.append(list)
print(list1)
    #self.assertListEqual(list1,['All','Enabled','Disabled'],'List values Matched')






