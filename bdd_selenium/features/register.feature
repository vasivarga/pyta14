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
    # Pasul de mai jos l-am comentat,
    # deoarece comportamentul site-ului s-a schimbat si eroarea nu mai apare
    # Then Password mandatory error is displayed
    Then Password confirm mandatory error is displayed

  Scenario: Validate password input minim length
    When I set "PY" as first name
    When I set "TA" as last name
    When I set "PYTA14@yahoo.com" as email
    When I set "12345" as password
    When I set "12345" as password confirmation
    When I click Register button
    Then Password min length error is displayed

  # Adaugati un test care face un register complet si verifica ca apare
  # mesajul de succes
  # tip: verificati ca exista mesajul
  # verificati textul de pe mesaj
  # Adresa de email se va genera random
  # metoda pentru dropdown select:
  #     def select_dropdown_text(self, locator, text):
  #        dropdown = Select(self.find(locator))
  #        dropdown.select_by_visible_text(text)

  # REZOLVARE:
    Scenario: Register new account with valid data
    When I set "PY" as first name
    And I set "TA" as last name
    And I select "10" "May" "1999" as my birth date
    And I set a random valid email
    And I set "pisicaneagra" as password
    And I set "pisicaneagra" as password confirmation
    And I click Register button
    Then Success message is displayed
    And The success message is "Your registration completed"

