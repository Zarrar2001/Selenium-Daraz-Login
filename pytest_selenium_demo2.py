import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Fix: Imported Keys properly

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager



@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Runs in headless mode (no UI)
    options.add_argument("--no-sandbox")  # Bypasses OS security model
    options.add_argument("--disable-dev-shm-usage")  # Prevents crashes in some environments

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# @pytest.fixture(params=["chrome","firefox","edge"])
# def driver(request):
#  browser = request.param
#  if browser == "chrome":
#
#    driver = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))
#  elif browser == "firefox":
#    driver = webdriver.Firefox(service= FirefoxService(GeckoDriverManager().install()))
#  elif browser == "edge":
#    driver = webdriver.Edge(service= EdgeService(EdgeChromiumDriverManager().install()))
#  else:
#      raise ValueError("Unsupported Browser!")
#  driver.implicitly_wait(10)
#  yield driver
#  driver.close()
#  driver.quit()
@pytest.mark.parametrize("email, password,expected_success",[
    ("hariskhan@gmail.com", "23455",False),
    ("zarrark@gmail.com", "6767",False),
    ("hk0991465@gmail.com", "Zarrar@2001",True)
])

def test_login(driver, email, password, expected_success):
 driver.get("https://www.daraz.pk/#?")
 login_button = driver.find_element("xpath", "//a[contains(text(),'Login')]")
 login_button.click()
 email_field = driver.find_element(By.XPATH,"//input[@placeholder='Please enter your Phone Number or Email']")
 password_field = driver.find_element(By.XPATH,"//input[@placeholder='Please enter your password']")
 submit_button = driver.find_element(By.XPATH,"//div[@class='iweb-button-mask']")

 email_field.send_keys(email)
 time.sleep(1)
 password_field.send_keys(password)
 time.sleep(1)
 submit_button.click()
 time.sleep(2)
 # login_success_text = "HK0991465'S ACCOUNT"
 # page_source = driver.page_source
 # assert login_success_text in page_source,"flogin failed for {email}"
 page_source = driver.page_source

 if expected_success:
     success_text = "HK0991465'S ACCOUNT"  # Change this if necessary
     assert success_text in page_source, f"Login failed for {email}"
     print(f"✅ Login PASSED for: {email}")
 else:
     error_text = "Invalid email or password"  # Change this to match Daraz's actual error message
     assert error_text in page_source, f"Unexpected login success for {email}"
     print(f"❌ Login FAILED as expected for: {email}")








