# pip install selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
time.sleep(1)

search_box = driver.find_element(By.ID, "small-searchterms")
search_box.send_keys("phone")
time.sleep(1)

search_box_2 = driver.find_element(By.CLASS_NAME, "search-box-text")
search_box_2.clear()
time.sleep(1)

search_box_3 = driver.find_element(By.NAME, "q")
search_box_3.send_keys("phone")
time.sleep(1)

link_register = driver.find_element(By.LINK_TEXT, "Register")
link_register.click()
time.sleep(1)


digital_downloads_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Digital")
digital_downloads_link.click()
time.sleep(1)

search_box = driver.find_element(By.ID, "small-searchterms")

element_picture = driver.find_element(By.CLASS_NAME, "picture")
# element_picture.click()

# Lista cu elementele care au clasa "picture"
lista_elemente = driver.find_elements(By.CLASS_NAME, "picture")
print(len(lista_elemente))


lista_elemente[1].click()

lista_2 = driver.find_elements(By.ID, "id_inexistent_in_pagina")
print(len(lista_2))

time.sleep(5)

# Assert verifica o expresie la care se asteapta sa fie True
# Daca expresia nu este adevarata, atunci programul se va opri
assert 3 + 2 == 5, "Expresia este falsa"

print("Am trecut de assert")

driver.quit()