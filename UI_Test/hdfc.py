import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


#browser = webdriver.Chrome("..\\Browser_Driver\\chromedriver.exe")
#browser = webdriver.Chrome()

#browser = webdriver.Firefox()



#browser = webdriver.Firefox(executable_path='C:\\Users\\admin\\PycharmProjects\\Python-selenium\\Browser_Driver\\geckodriver.exe')
#browser = webdriver.Chrome(executable_path="C:\\Users\\admin\\PycharmProjects\\Python-selenium\\Browser_Driver\\chromedriver.exe")
browser = webdriver.Chrome(ChromeDriverManager().install())
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#browser = webdriver.Edge(EdgeChromiumDriverManager().install())

browser.get("https://netbanking.hdfcbank.com/netbanking/?_ga=2.206344148.634710112.1622004356-1989136729.1622004356")
browser.switch_to_frame("login_page")
user_id =browser.find_element_by_xpath("//input[@name='fldLoginUserId']")
conti =browser.find_element_by_xpath("//img[@src='/gif/continue_new1.gif?v=1']")
#login = browser.find_element_by_xpath("//input[@id='btnLogin']")
user_id.send_keys()
#password.send_keys("admin123")
conti.click()
# wait = WebDriverWait(browser,20)
#
# page_title =browser.title

alert = Alert(browser)
print(alert.text)
time.sleep(5)
alert.accept()



