import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(1)

# EX1:

search_box = driver.find_element(By.ID, "small-searchterms")
search_box.send_keys("phone")

button_search = driver.find_element(By.CLASS_NAME, "search-box-button")
button_search.click()

time.sleep(2)

price_list = driver.find_elements(By.CSS_SELECTOR, "span.actual-price")
price_value_list = []

for element in price_list:
    text = element.text
    # $300.00
    value = float(text.replace("$", ""))
    price_value_list.append(value)

price_value_list.sort()

print(price_value_list[0])

# EX 2:

assert driver.title == "nopCommerce demo store. Search"

# EX 3:

driver.find_element(By.CSS_SELECTOR, "a.ico-login").click()
time.sleep(1)

url_before_login = driver.current_url

driver.find_element(By.ID, "Email").send_keys("pyta14@gmail.com")
driver.find_element(By.ID, "Password").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, "button.login-button").click()

url_after_login = driver.current_url

expected_error_text = "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"
actual_error_text = driver.find_element(By.CSS_SELECTOR, "div.message-error").text

assert url_before_login.lower() in url_after_login.lower(), "Error, unexpected url after click on login button"
assert expected_error_text == actual_error_text, "Error, unexpected error message"


# Ex 4
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("pyta14")
driver.find_element(By.ID, "Password").click()

email_error = driver.find_element(By.ID, "Email-error")
assert email_error.is_displayed(), "Error, email error message not displayed"
assert email_error.text == "Wrong email", "Unexpected error text"

# EX 5

# TC: Se face o cautare dupa care sortam rezultatee gasite in ordine crescatoare

search_box = driver.find_element(By.ID, "small-searchterms")
search_box.send_keys("phone")

button_search = driver.find_element(By.CLASS_NAME, "search-box-button")
button_search.click()
time.sleep(2)

dropdown_sort = Select(driver.find_element(By.ID, "products-orderby"))
dropdown_sort.select_by_visible_text("Price: Low to High")
time.sleep(3)

price_list = driver.find_elements(By.CSS_SELECTOR, "span.actual-price")
price_value_list = []

for element in price_list:
    text = element.text
    # $300.00
    value = float(text.replace("$", ""))
    price_value_list.append(value)

price_value_list_initial = list.copy(price_value_list)
price_value_list.sort()

assert price_value_list_initial == price_value_list, "Error, sorting is not working properly"
