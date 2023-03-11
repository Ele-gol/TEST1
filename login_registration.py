#import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# driver = webdriver.Chrome(chrome_options=chrome_options)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://practice.automationtesting.in")
# account = driver.find_element_by_link_text("My Account").click()
# email = driver.find_element_by_css_selector("#reg_email").send_keys("boris@yandex.ru")
# Password = driver.find_element_by_css_selector("#reg_password").send_keys("Qaz123567Zx13042016")
# register = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row").click()
# time.sleep(5)
# driver.quit()
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://practice.automationtesting.in")
account = driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_css_selector("#username").send_keys("boris@yandex.ru")
Password = driver.find_element_by_css_selector("#password").send_keys("Qaz123567Zx13042016")
login_btn = driver.find_element_by_name("login").click()
logout_element = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout"), "Logout"))
time.sleep(5)
driver.quit()
