Feature: OrangeHrm Logo
  Scenario: Logo presence on OrangeHrm feature
    Given launch chrome browser
    When  open OrangeHrm home page
    Then verify that logo present on homepage
    And close browser
