Feature: OrangeHRM Login

  Scenario: Login to HRM Application
    Given I launch browser
    When I open application
    And Enter valid username and password
    And click on login
    Then User must login to the Dashboard page

  Scenario: Search user
    Given I launch browser
    When I open application
    And Enter valid username and password
    And click on login
    When navigate to search page
    Then search page should display

  Scenario: Advanced Search user
    Given I launch browser
    When I open application
    And Enter valid username and password
    And click on login
    When navigate to advanced search page
    Then advanced search page should display