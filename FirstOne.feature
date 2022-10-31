Feature: Login Page

  Scenario: User Login - error cases
    Given I access the login page
    When I hit the login button
    Then I got an "error"
