Feature: Login

  Scenario: Log in with invalid credentials
    Given I am on the login page
    When I enter an invalid email
    And I enter a password
    And I click the login button
    Then An error message is displayed
    And I should see "No customer account found"