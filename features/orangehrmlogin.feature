Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open orange HRM Homepage
    And Enter username "admin" and password "admini23"
    And Click on login button
    Then User must successfully login to theDashboard page