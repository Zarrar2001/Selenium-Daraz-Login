# from selenium import webdriver
#
# # Set the remote WebDriver URL (change browser as needed)
# grid_url = "http://localhost:4444/wd/hub"
#
# # Define desired capabilities for Chrome
# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Remote(command_executor=grid_url, options=chrome_options)
#
# # Open a website
# driver.get("https://www.google.com")
#
# # Print title to verify it works
# print("Page Title:", driver.title)
#
# # Close the browser

# driver.quit()
#
import pytest
from selenium import webdriver
import time


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_open_google(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        time.sleep(2)
    elif browser == "firefox":
        driver = webdriver.Firefox()
        time.sleep(2)

    driver.get("https://www.google.com")
    print(f"{browser.capitalize()} Page Title:", driver.title)
    driver.quit()

