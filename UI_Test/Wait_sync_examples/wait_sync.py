from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager




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

browser.find_element_by_partial_link_text("Welcome").click()
browser.implicitly_wait(10)
# wait =WebDriverWait(browser,10)
# wait.until(EC.element_to_be_clickable(By.XPATH,"//a[text()='Logout']"))
browser.find_element_by_xpath("//a[text()='Logout']").click()
element = browser.find_element_by_xpath("//div[@id='logInPanelHeading']")
element.is_displayed()






