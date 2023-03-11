# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in")
# element = driver.find_element_by_css_selector(".post-160.product.type-product.status-publish").click()
# reviews_btn = driver.find_element_by_css_selector(".reviews_tab").click()
# five = driver.find_element_by_css_selector(".star-5").click()
# reviews = driver.find_element_by_css_selector("#comment").send_keys("Nice book1!")
# Name = driver.find_element_by_css_selector("#author").send_keys("Boris")
# Email = driver.find_element_by_css_selector("#email").send_keys("boris@yandex.ru")
# sambit_btn = driver.find_element_by_css_selector(".submit").click()

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://practice.automationtesting.in")
driver.execute_script("window.scrollBy(0,600);")
element = driver.find_element_by_css_selector(".post-160.product.type-product.status-publish").click()
reviews_btn = driver.find_element_by_css_selector(".reviews_tab").click()
five = driver.find_element_by_css_selector(".star-5").click()
reviews = driver.find_element_by_css_selector("#comment").send_keys("Nice book!!!!")
Name = driver.find_element_by_css_selector("#author").send_keys("Boris")
Email = driver.find_element_by_css_selector("#email").send_keys("boris@yandex.ru")
sambit_btn = driver.find_element_by_css_selector(".submit").click()
time.sleep(5)
driver.quit()


