Feature: Create a new sales order

  Scenario: Successfully create a new sales order
    Given I open the sales order page
    When I fill in the customer details
    And I add an item to the order
    And I select a payment method
    And I set the expected delivery date
    And I click on "Create Order"
    Then the order should be created successfully
