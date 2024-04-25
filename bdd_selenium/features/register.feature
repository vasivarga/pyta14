Feature: Register

  Background: Open register page
    Given I am on the Register page

  # Shortcut pentru duplicare de linie CTRL + D
  @regression
  Scenario: Check validation for mandatory fields
    When I click Register button
    Then First name mandatory error is displayed
    Then Last name mandatory error is displayed
    Then Email mandatory error is displayed
    Then Password mandatory error is displayed
    Then Password confirm mandatory error is displayed

  Scenario: Validate password input minim length
    When I enter "12345" as password
    When I click outside the password field
    Then Password min length error is displayed

  # Adaugati un test care face un register complet si verifica ca apare mesajul de succes
  # tip: verificati ca exista mesajul
  # verificati textul de pe mesaj
  # Adresa de email se va genera random
  # metoda pentru dropdown select:
  #     def select_dropdown_text(self, locator, text):
  #        dropdown = Select(self.find(locator))
  #        dropdown.select_by_visible_text(text)

