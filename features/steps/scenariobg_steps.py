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


@when('Enter valid username and password')
def enter_information(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")


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
def search_page(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").click()
    assert True, "Test Passed!!!"


@then('search page should display')
def validate_search_page(context):
    status = context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").is_displayed()
    assert status is True


@when('navigate to advanced search page')
def advanced_search_page(context):
    context.driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click()


@then(u'advanced search page should display')
def validate_advanced_search_page(context):
    text = context.driver.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 oxd-table-filter-title']").text
    if text == "System Users":
        assert True, "Test Passed!!!"
    else:
        assert False, "Test Failed!!!"

