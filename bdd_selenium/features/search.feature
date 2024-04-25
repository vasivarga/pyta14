Feature: Search

  Background: Open home page
    Given I am on the home page

  Scenario: Search works properly
    When I enter "HTC" in the search field
    And I click the search button
    Then I am redirected to the search results page
    And There are some results displayed
    # Transformati scenariul in Scenario Outline
    # In felad-ul de cautare introduceti minim 3 nume de produse care returneaza un rezultat