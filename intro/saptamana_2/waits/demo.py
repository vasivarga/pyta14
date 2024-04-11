import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
driver.maximize_window()

# EXERCITIU Wait Implicit
# - Click pe butonul "Change Text to Selenium Webdriver"
# - Dupa 10 secunde textul "site" se va schimba in "Selenium Webdriver"
# - Vom folosi un implicit wait pentru a face driverul sa astepte maxim 11 secunde inainte sa dea eroare
driver.find_element(By.ID, "populate-text").click()
time.sleep(10)
driver.implicitly_wait(20)
element_gasit = driver.find_element(By.XPATH, "//h2[text()='Selenium Webdriver']")

driver.implicitly_wait(0)
# element_gasit_2 = driver.find_element(By.XPATH, "//h2[text()='Selenium Webdriver INEXISTENT']")

# EXERCITIU Wait Explicit
# Deoarece elementul se afla deja in pagina si este invizibil,
# wait-ul implicit nu ne ajuta
# Vom folosi un wait explicit care asteapta ca elementul sa devina vizibil
hidden_button = driver.find_element(By.ID, "hidden")

driver.find_element(By.ID, "display-other-button").click()

# Declarare wait explicit - inca nu se declanseaza procesul de asteptare
wait = WebDriverWait(driver, 20)

# Aici incepem sa asteptam
wait.until(expected_conditions.visibility_of(hidden_button))

hidden_button.click()
