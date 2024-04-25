Feature: Login

  Background: Open login page
    Given I am on the login page

  @smoke @regression
  Scenario: Check that the URL of the page is correct
    Then The URL of the page is "https://demo.nopcommerce.com/login"

  # Tema: Implementati un test similar pentru verificarea titlului paginii

  @regression
  Scenario Outline: Log in with invalid credentials
    When I enter "<username>" as username
    And I enter "<password>" as password
    And I click the login button
    Then An error message is displayed
    And I should see "No customer account found"
    Examples:
      | username         | password     |
      | pyta14@gmail.com | 12345678     |
      | pyta14@yahoo.com | fhjkdshfjksf |
      | pyta14@bing.com  | efkdshfdfgjk |
