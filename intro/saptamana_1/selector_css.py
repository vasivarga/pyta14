import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

# search_box = driver.find_element(By.CSS_SELECTOR, "#small-searchterms")
# search_box.send_keys("phone")

driver.find_element(By.CSS_SELECTOR, "#small-searchterms").send_keys("phone")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name='q']").clear()

driver.find_element(By.CSS_SELECTOR, "input[type='text'][placeholder='Search store']").send_keys("Laptop")
time.sleep(1)

driver.get("https://formy-project.herokuapp.com/form")
time.sleep(1)


dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#select-menu"))
dropdown.select_by_visible_text("2-4")
time.sleep(1)

dropdown.select_by_index(1)
time.sleep(1)

dropdown.select_by_value("4")
time.sleep(3)





driver.quit()