# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# options = Options()
# options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options= options)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"openwindow").click()
# time.sleep(2)
# print(driver.window_handles)
# print("***********")
# driver.find_element(By.ID,"opentab").click()
# time.sleep(2)
# print(driver.window_handles)
# driver.quit()
import time
import pytest  # ✅ Import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture  # ✅ Setup and teardown WebDriver
def setup():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver  # ✅ Provides the driver instance
    driver.quit()  # ✅ Cleanup after test execution

def test_multiple_windows(setup):  # ✅ Function name starts with test_
    driver = setup
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(2)
    frame_element = driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']")
    driver.switch_to.frame(frame_element)
    time.sleep(2)
    driver.find_element("xpath","//a[conatains(text()='Job Support']")


    # driver.find_element(By.ID, "openwindow").click()
    # time.sleep(3)
    # print("Windows after opening 'Open Window':", driver.window_handles)
    #
    # driver.find_element(By.ID, "opentab").click()
    # time.sleep(3)
    # print("Windows after opening 'Open Tab':", driver.window_handles)
    # driver.switch_to.window(driver.window_handles[1])
    # driver.find_element("xpath","//a[@href='https://www.qaclickacademy.com/blog']").click()
    #
    #



