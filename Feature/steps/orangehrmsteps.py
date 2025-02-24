# # You can implement step definitions for undefined steps with these snippets:
# from behave import *
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# @given('launch chrome browser')
# def launchBrowser(context):
#     options = Options()
#     context.driver = webdriver.Chrome(options=Options)
#
#
#
# @when('open OrangeHrm home page')
# def openHomePage(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#
#
#
# @then('verify that logo present on homepage')
# def verifyLogo(context):
#     status = context.driver.find_element("xpath" , ("//img[@alt='company-branding']").is_displayed())
#     assert status is True
#
#
# @then('close browser')
# def closeBrowser(context):
#     context.driver.close()
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launchBrowser(context):
    options = Options()  # ✅ Correct way to use Options
    context.driver = webdriver.Chrome(options=options)

@when('open OrangeHrm home page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

@then('verify that logo present on homepage')
def verifyLogo(context):
    logo = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']")
    assert logo.is_displayed()

@then('close browser')
def closeBrowser(context):
    context.driver.quit()
