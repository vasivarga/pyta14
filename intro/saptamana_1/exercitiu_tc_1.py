import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(1)

search_box = driver.find_element(By.ID, "small-searchterms")
search_box.send_keys("phone")

button_search = driver.find_element(By.CLASS_NAME, "search-box-button")
button_search.click()
time.sleep(2)

results_list = driver.find_elements(By.CLASS_NAME, "item-box")
results_size = len(results_list)

assert results_size >= 3, "Test failed, there are less than 3 elements"