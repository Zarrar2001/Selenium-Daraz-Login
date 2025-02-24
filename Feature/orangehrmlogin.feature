Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameters
    Given I launch the chrome browser
    When I open orange HRM homepage
    And Enter username "admin" and password "admin123"
    And Click on Login button
    Then  User must successfully login to Dashboard page