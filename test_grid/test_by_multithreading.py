
import threading
from selenium import webdriver

def run_test(browser):
    """Function to run a test in a specific browser."""
    grid_url = "http://localhost:4444/wd/hub"
    options = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

    driver = webdriver.Remote(command_executor=grid_url, options=options)
    driver.get("https://www.google.com")
    print(f"Page Title on {browser}: {driver.title}")
    driver.quit()

# Creating threads for Chrome and Firefox
chrome_thread = threading.Thread(target=run_test, args=("chrome",))
firefox_thread = threading.Thread(target=run_test, args=("firefox",))

# Starting threads
chrome_thread.start()
firefox_thread.start()

# Waiting for both threads to complete
chrome_thread.join()
firefox_thread.join()
