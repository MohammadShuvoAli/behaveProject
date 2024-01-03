from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def open_chrome_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('I open orange HRM Homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{username}" and password "{password}"')
def enter_information(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)


@when('Click on login button')
def click_login(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must successfully login to the Dashboard page')
def login_validation(context):
    text = context.driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    assert text == "Dashboard"
    context.driver.quit()
