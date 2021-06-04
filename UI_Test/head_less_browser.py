import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
opt =Options()
#opt.__setattr__('headless',True)
opt.add_argument('incognito')

browser = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
browser.get("https://the-internet.herokuapp.com/javascript_alerts")
browser.find_element_by_xpath("//button[text()='Click for JS Alert']").click()
alert=Alert(browser)
alert_mssage=alert.text
print(alert_mssage)
time.sleep(3)
alert.accept()
result=browser.find_element_by_id("result").text
assert result=="You successfully clicked an alert"

browser.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
alert=Alert(browser)
alert_mssage=alert.text
print(alert_mssage)
time.sleep(3)
alert.accept()
result=browser.find_element_by_id("result").text
assert result=="You clicked: Ok"

browser.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
alert=Alert(browser)
time.sleep(3)
alert.send_keys("Rajashekar")

time.sleep(3)
alert.accept()
result=browser.find_element_by_id("result").text
print(result)
assert result=="You entered: Rajashekar"
browser.close()







