# import pytest
# import  time
# from selenium import webdriver
# from selenium import Keys
# from selenium.webdriver.chrome.service import  Service as ChromeService
# from  selenium.webdriver.common.by import By
# import webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Fix: Imported Keys properly

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Fix: Corrected import

# Initialize WebDriver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))





@pytest.fixture()
def driver():
 driver = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))
 driver.implicitly_wait(10)
 yield driver
 driver.close()
 driver.quit()
def test_google_search(driver):
  driver.get("https://www.google.com/")
  googleSearchBox = driver.find_element(By.ID,"APjFqb")
  googleSearchBox .send_keys("Automation")
  googleSearchBox.send_keys(Keys.RETURN)
  time.sleep(2)
  print("Test completed")


