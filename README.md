** Project Structure **

PurePythonProject/
│── features/
│   │── steps/
│   │   │── calculator_steps.py
│   │   │── login_steps.py
│   │   │── <new_module>_steps.py  # Add new module steps here
│   │
│   │── calculator.feature
│   │── login.feature
│   │── <new_module>.feature       # Add new module feature file here
│
│── include/
│── lib/
│── requirements.txt

---------------------------------------------------------------------->>>

#Steps to Follow for New Modules
##Create Feature File (.feature)

Place it inside the features/ folder.
Follow Gherkin syntax:

Feature: <New Module Name>
    Scenario: <Scenario Description>
        Given <Pre-condition>
        When <Action>
        Then <Expected Outcome>

Example (payment.feature):

Feature: Payment Processing
    Scenario: Successful Payment
        Given the user is on the checkout page
        When they enter valid payment details
        Then the payment should be successful

#Create Step Definition (_steps.py)

Place it inside features/steps/.
Implement step definitions using Behave:

from behave import given, when, then

@given("the user is on the checkout page")
def step_given_checkout(context):
    pass  # Implement logic

@when("they enter valid payment details")
def step_when_payment(context):
    pass  # Implement logic

@then("the payment should be successful")
def step_then_success(context):
    pass  # Implement logic
