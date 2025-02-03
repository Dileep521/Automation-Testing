Feature: Login functionality
  As a user
  I want to log into the application
  So that I can access my account

  Scenario: Successful login
    Given I open the login page
    When I input username "caremedics001+jan2@gmail.com"
    And I input password "Dileep@521"
    And I click the "Login" button
    Then I should see a welcome message "Welcome, testuser!"

  Scenario: Unsuccessful login with incorrect credentials
    Given I open the login page
    When I input username "testuser"
    And I input password "wrongpassword"
    And I click the "Login" button
    Then I should see an error message "Invalid username or password"

  Scenario: Unsuccessful login with empty fields
    Given I open the login page
    When I click the "Login" button
    Then I should see an error message "Username and password are required"