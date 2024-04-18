# 1. Deschidem browserul și intrăm pe https://magento.softwaretestingboard.com/
# 2. Acceptăm termenii și condițiile
# 3. Căutăm produse după cuvântul “jacket”
# 4. Identificăm primul produs dintre rezultate și facem click pe numele acestuia ca sa
# deschidem pagina produsului
# 5. Alegem mărimea XS
# 6. Alegem culoarea gri
# 7. Adaugam produsul in cos
# 8. Validăm (assert) că avem 1 articol în coș
# 9. Facem click pe cos
# 10. Validăm (assert) că numele produsului din coș coincide cu numele produsului din pagină
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/")
driver.find_element(By.CLASS_NAME, "fc-cta-consent").click()
driver.find_element(By.ID, "search").send_keys("jacket" + Keys.ENTER)
driver.find_element(By.CLASS_NAME, "product-item-link").click()
driver.find_element(By.XPATH, "//div[@aria-label='XS']").click()
driver.find_element(By.CSS_SELECTOR, "div[aria-label='Gray']").click()
driver.find_element(By.ID, "product-addtocart-button").click()
COUNTER_LOCATOR = (By.CLASS_NAME, "counter-number")

wait = WebDriverWait(driver, 3)
wait.until(expected_conditions.text_to_be_present_in_element(COUNTER_LOCATOR, "1"))

quantity = driver.find_element(*COUNTER_LOCATOR).text
assert quantity == "1", f"Wrong quantity. \nExpected: 1, \nActual: {quantity}"

driver.find_element(*COUNTER_LOCATOR).click()

product_name_in_page = driver.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
product_name_in_cart = driver.find_element(By.CSS_SELECTOR, "[class='product-item-name']").text

assert product_name_in_page == product_name_in_cart, "Add to cart validation failed."

time.sleep(3)



