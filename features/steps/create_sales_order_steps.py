from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from behave import given, when, then
from selenium.webdriver.edge.service import Service


# Initialize WebDriver
@given("I open the sales order page")
def open_sales_order_page(context):
    service = Service("C:/Users/DivithM/Desktop/Driver/msedgedriver.exe")  # Replace with the actual path
    context.driver = webdriver.Edge(service=service)
    context.driver.maximize_window()
    context.driver.get("https://stagingaz.ezscm.ai/")  # Replace with your actual URL
    sleep(2)
    print("Step 1: Opened login page")

    context.driver.find_element(By.XPATH, "//li[normalize-space()='Sales Orders']").click()
    print("Step 2: Redirected tp Sales Orders page")


@when("I fill in the customer details")
def fill_customer_details(context):
    context.driver.find_element(By.NAME, "phoneNumber").send_keys("+919876543210")
    context.driver.find_element(By.NAME, "firstName").send_keys("John")
    context.driver.find_element(By.NAME, "lastName").send_keys("Doe")
    context.driver.find_element(By.NAME, "address").send_keys("123 Main Street")
    Select(context.driver.find_element(By.NAME, "country")).select_by_visible_text("India")
    Select(context.driver.find_element(By.NAME, "state")).select_by_visible_text("Maharashtra")
    Select(context.driver.find_element(By.NAME, "city")).select_by_visible_text("Mumbai")


@when("I add an item to the order")
def add_item(context):
    Select(context.driver.find_element(By.NAME, "item")).select_by_visible_text("Product A")
    qty_field = context.driver.find_element(By.NAME, "quantity")
    qty_field.clear()
    qty_field.send_keys("2")
    sleep(1)


@when("I select a payment method")
def select_payment_method(context):
    Select(context.driver.find_element(By.NAME, "paymentMethod")).select_by_visible_text("Credit Card")


@when("I set the expected delivery date")
def set_delivery_date(context):
    date_field = context.driver.find_element(By.NAME, "deliveryDate")
    date_field.send_keys("2025-02-20")
    sleep(1)


@when("I click on \"Create Order\"")
def click_create_order(context):
    context.driver.find_element(By.ID, "createOrderButton").click()
    sleep(3)


@then("the order should be created successfully")
def verify_order_creation(context):
    success_msg = context.driver.find_element(By.CLASS_NAME, "success-message").text
    assert "Order created successfully" in success_msg
    context.driver.quit()
