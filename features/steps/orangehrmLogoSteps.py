from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://www.orangehrm.com/")


@then('verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, "//img[@src='/_resources/themes/orangehrm/dist/images/OrangeHRM_Logo.svg']").is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.quit()
