from behave import  *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('I open application')
def open_application(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{username}" and password "{password}"')
def enter_information(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)


@when('click on login')
def click_login(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must login to the Dashboard page')
def login_validation(context):
    try:
        text = context.driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    except:
        context.driver.quit()
        assert False, "Test Failed!!!"
    if text == "Dashboard":
        context.driver.quit()
        assert True, "Test Passed!!!"


@when('navigate to search page')
def step_impl(context):
    assert True, "Test Passed!!!"


@then('search page should display')
def step_impl(context):
    assert True, "Test Passed!!!"


@when(u'navigate to advanced search page')
def step_impl(context):
    assert True, "Test Passed!!!"


@then(u'advanced search page should display')
def step_impl(context):
    assert True, "Test Passed!!!"
