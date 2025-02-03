from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I open the login page")
def open_login_page(context):
    service = Service("C:/Users/DivithM/Desktop/Driver/msedgedriver.exe")  # Replace with the actual path
    context.driver = webdriver.Edge(service=service)
    context.driver.maximize_window()
    context.driver.get("https://stagingaz.ezscm.ai/")  # Replace with your actual URL
    print("Step 1: Opened login page")


@when('I input username "{username}"')
def input_username(context, username):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    ).send_keys(username)
    print("Step 2: Entered username")


@when('I input password "{password}"')
def input_password(context, password):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    ).send_keys(password)
    print("Step 3: Entered password")


@when('I click the "Login" button')
def click_login_button(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log in']"))
    ).click()
    print("Step 4: Clicked login button")


@then('I should see a welcome message "{message}"')
def verify_welcome_message(context, message):
    welcome_text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "welcome-message"))  # Replace with the actual ID for the welcome message
    ).text
    assert welcome_text == message, f"Expected '{message}', but got '{welcome_text}'"
    print("Step 5: Verified welcome message")


@then('I should see an error message "{message}"')
def verify_error_message(context, message):
    error_text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Toastify__toast-body') and contains(text(), 'Invalid username or password')]"))
    ).text
    assert error_text == message, f"Expected '{message}', but got '{error_text}'"
    print("Step 6: Verified error message")


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
    print("Step 7: Browser closed")