
import time
from selenium.webdriver.support import expected_conditions as EC

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@given('I launch the chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open orange HRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(user)
    context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(pwd)
    time.sleep(3)


@when('Click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(3)


@then('User must successfully login to Dashboard page')
def step_impl(context):
    try:
        dashboard_element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[contains(text(), 'Dashboard')]"))
        )  # ✅ Wait for Dashboard to appear
        assert dashboard_element.text == "Dashboard", "Login failed!"
    finally:
        context.driver.quit()  # ✅ Close browser after test

