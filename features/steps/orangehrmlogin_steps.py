from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@placeholder='username']").send_keys(username)
    context.driver.find_element(By.XPATH, "//input[@placeholder='password']").send_keys(password)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must successfully login to theDashboard page')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    assert text == "Dashboard"
    context.driver.quit()
