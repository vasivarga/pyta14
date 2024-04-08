import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#TC: Completarea formularului

# Rezultate asteptate:
# - linkul schimbat in https://formy-project.herokuapp.com/thanks
# - mesaj de succes afisat
# - textul mesajului de succes: The form was successfully submitted!

driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/form")

driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Mihai")
time.sleep(2)

driver.find_element(By.XPATH, "(//input)[2]").send_keys("Pop")
driver.find_element(By.XPATH, "//input[@placeholder='Enter your job title']").send_keys("QA Engineer")
driver.find_element(By.XPATH, "//input[@type='radio' and @value='radio-button-3']").click()
driver.find_element(By.XPATH, "//input[@value='checkbox-1']")
dropdown_select = Select(driver.find_element(By.XPATH, "//select[@id='select-menu']"))
dropdown_select.select_by_visible_text("2-4")
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
driver.find_element(By.XPATH, "//td[@class='today day']/following-sibling::td | //td[@class='today day']/../following-sibling::tr/td[1]").click()
driver.find_element(By.XPATH, "//a[text()='Submit']").click()
time.sleep(1)

success_message = driver.find_element(By.XPATH, "//div[@role='alert']")

assert driver.current_url == "https://formy-project.herokuapp.com/thanks", "Eroare, URL-ul este incorect"
assert success_message.is_displayed(), "Eroare, mesajul de succes nu este afisat!"
assert success_message.text == "The form was successfully submitted!", "Eroare, textul de pe element nu este corect"
time.sleep(3)
driver.quit()