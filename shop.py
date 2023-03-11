# import time
# from selenium import webdriver
# from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
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
# login = driver.find_element_by_css_selector("#username").send_keys("boris@yandex.ru")
# Password = driver.find_element_by_css_selector("#password").send_keys("Qaz123567Zx13042016")
# login_btn = driver.find_element_by_name("login").click()
# shop = driver.find_element_by_link_text("Shop").click()
# html5  = driver.find_element_by_partial_link_text("Forms").click()
# text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))
# time.sleep(5)
# driver.quit()

#
# import time
# from selenium import webdriver
# from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://practice.automationtesting.in")
# account = driver.find_element_by_link_text("My Account").click()
# login = driver.find_element_by_css_selector("#username").send_keys("boris@yandex.ru")
# Password = driver.find_element_by_css_selector("#password").send_keys("Qaz123567Zx13042016")
# login_btn = driver.find_element_by_name("login").click()
# shop = driver.find_element_by_link_text("Shop").click()
# HTML = driver.find_element_by_link_text("HTML").click()
# number = driver.find_elements_by_css_selector("#pagewrap")
# driver.find_elements_by_css_selector(".button.product_type_simple.ajax_add_to_cart")
# if len(items_count)==3:
#     print("На странице 3 товара")
# else:
    # print("Ошибка")
# time.sleep(5)
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://practice.automationtesting.in")
# account = driver.find_element_by_link_text("My Account").click()
# login = driver.find_element_by_css_selector("#username").send_keys("boris@yandex.ru")
# Password = driver.find_element_by_css_selector("#password").send_keys("Qaz123567Zx13042016")
# login_btn = driver.find_element_by_name("login").click()
# shop = driver.find_element_by_link_text("Shop").click()
# options = driver.find_element_by_css_selector("[value=menu_order]")
# price = driver.find_element_by_tag_name("select").click()
# price = driver.find_element_by_css_selector("option:nth-child(6)").click()
# price = driver.find_element_by_css_selector("option:nth-child(6)")
# price = WebDriverWait(driver,5).until(EC.element_to_be_selected(price))
# time.sleep(5)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.get("https://practice.automationtesting.in")
# account = driver.find_element_by_link_text("My Account").click()
# login = driver.find_element_by_css_selector("#username").send_keys("boris@yandex.ru")
# Password = driver.find_element_by_css_selector("#password").send_keys("Qaz123567Zx13042016")
# login_btn = driver.find_element_by_name("login").click()
# shop = driver.find_element_by_link_text("Shop").click()
# book = driver.find_element_by_css_selector(".post-169.product.type-product.status-publish.product_cat-android.product_tag-android").click()
# book_old_price = driver.find_element_by_css_selector(".price>del>span")
# book_old_price_text = book_old_price.text
# assert book_old_price_text == "₹600.00"
# book_new_price = driver.find_element_by_css_selector(".price>ins>span")
# book_new_price_text = book_new_price.text
# assert book_new_price_text == "₹450.00"
# book_btn = WebDriverWait(driver, 10).until
# (EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-main-image.zoom"),"Android Quick Start Guide"))
# book_btn = driver.find_element_by_css_selector(".woocommerce-main-image.zoom").click()
# close = driver.find_element_by_css_selector(".pp_close").click()
# time.sleep(5)
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in")
# shop = driver.find_element_by_link_text("Shop").click()
# book = driver.find_element_by_css_selector(".button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
# time.sleep(5)
# element = driver.find_element_by_css_selector(".cartcontents")
# element_get_text = element.text
# assert element_get_text == "1 Item"
# element2 = driver.find_element_by_css_selector("#wpmenucartli")
# element2_get_text = element2.text
# assert "350.00" in element2_get_text
# element = driver.find_element_by_css_selector(".cartcontents").click()
# subtotal_text_ = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cart-subtotal"), "350.00" ))
# Total_text = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".order-total"),"357.00"))
# time.sleep(5)
# driver.quit()

#
# import time
# from selenium import webdriver
# from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://practice.automationtesting.in")
# shop = driver.find_element_by_link_text("Shop").click()
# driver.execute_script("window.scrollBy(0,300);")
# book = driver.find_element_by_css_selector(".button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
# time.sleep(5)
# element = driver.find_element_by_css_selector(".cartcontents").click()
# time.sleep(5)
# delete = driver.find_element_by_css_selector("a.remove").click()
# undo = driver.find_element_by_link_text("Undo?").click()
# option = driver.find_element_by_css_selector("[value='1']").clear()
# time.sleep(5)
# option = driver.find_element_by_css_selector(".input-text.qty.text")
# option.send_keys("3")
# update_btn =driver.find_element_by_name("update_cart").click()
# option = driver.find_element_by_css_selector(".input-text.qty.text")
# option_get_text = option.text
# assert option_get_text != 0
# time.sleep(5)
# apply_btn = driver.find_element_by_css_selector("[value='Apply Coupon']").click()
# please_text_ = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-error"), "Please enter a coupon code."))
# time.sleep(5)
# driver.quit()
#
# #
import time
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://practice.automationtesting.in")
shop = driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0,300);")
book = driver.find_element_by_css_selector(".button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
time.sleep(5)
element = driver.find_element_by_css_selector(".cartcontents").click()
time.sleep(5)
proceed = driver.find_element_by_css_selector(".checkout-button.button.alt.wc-forward").click()
time.sleep(5)
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("boris")
last_name = driver.find_element_by_css_selector("#billing_last_name")
last_name.send_keys("boris")
email = driver.find_element_by_id("billing_email")
email.send_keys("boris@yandex.ru")
tel = driver.find_element_by_id("billing_phone")
tel.send_keys("8888888888")
time.sleep(5)
element = driver.find_element_by_css_selector(".country_to_state.country_select:nth-child(2)").click()
element2 = driver.find_element_by_css_selector("#s2id_autogen1_search").send_keys("Afghanistan")
element2 = driver.find_element_by_css_selector(".select2-results-dept-0.select2-result.select2-result-selectable").click()
addres = driver.find_element_by_name("billing_address_1")
addres.send_keys("Aveny")
postcode = driver.find_element_by_name("billing_postcode")
postcode.send_keys("446092")
city = driver.find_element_by_name("billing_city")
city.send_keys("Иллинойс")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(5)
option_btn = driver.find_element_by_css_selector("#payment_method_cheque")
driver.execute_script("arguments[0].click();", option_btn)
placeorder_btn = driver.find_element_by_css_selector("#place_order")
driver.execute_script("arguments[0].click();", placeorder_btn)
thank_element = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check_element = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details"), "Check Payments"))
time.sleep(5)
driver.quit()