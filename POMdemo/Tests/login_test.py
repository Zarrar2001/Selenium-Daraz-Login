import  pytest
import  time
from  selenium import webdriver
from  selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from POMdemo.Tests.Pages.login_page import LoginPage
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.enter_password("password")
    time.sleep(1)
    login_page.enter_username("username")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    assert "Google" in driver.page_source
    time.sleep(1)
    # login_page.open_page("https://trytestingthis.netlify.app/")
    # driver.get("https://trytestingthis.netlify.apdocker pull selenium/hubp/")
    # username_field = driver.find_element(By.ID,"fname")
    # password_field = driver.find_element(By.ID,"lname")
    # submit_button = driver.find_element(By.XPATH,"//button[contains(@class, 'btn-success')]")
    # username_field.send_keys(username)
    # password_field.send_keys(password)

