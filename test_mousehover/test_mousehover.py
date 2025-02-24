# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome .options import Options
# from  selenium.webdriver.common.action_chains import ActionChains
# options = Options()
# options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options= options)
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH,"//button[text() = 'x']")))
# login_popup_close_button = driver.find_element("xpath","//button[text() = 'x']")
# login_popup_close_button.click()
# actions = ActionChains(driver,duration=2000)
# more_element = driver.find_element("xpath","//span[text()='Two Wheelers']")
# actions.move_to_element(more_element).click().perform()
# electric_vehicles = driver.find_element("xpath","//a[text()='Electric Vehicles']")
# actions.click(electric_vehicles).perform()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
#
# options = Options()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
#
# # Try to close the login popup
# try:
#     close_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='✕']"))
#     )
#     close_button.click()
# except Exception as e:
#     print("Login popup did not appear or could not be closed.")
#
# # Perform mouse hover
# actions = ActionChains(driver)
# more_element = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, "//span[text()='Two Wheelers']"))
# )
# actions.move_to_element(more_element).perform()
#
# # Click on "Electric Vehicles"
# electric_vehicles = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[text()='Electric Vehicles']"))
# )
# electric_vehicles.click()
#
# print("Test completed successfully!")
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="module")
def setup_browser():
    """Setup browser instance for the test"""
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    yield driver
    driver.quit()  # Close browser after test
#
#
# def test_mouse_hover(setup_browser):
#     """Test hover and click functionality"""
#     driver = setup_browser
#
#     # Close the login popup if present
#     try:
#         close_button = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[text()='✕']"))
#         )
#         close_button.click()
#     except Exception as e:
#         print("Login popup did not appear or could not be closed.")
#
#     # Hover over 'Two Wheelers'
#     more_element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//span[text()='Two Wheelers']"))
#     )
#
#     # Scroll into view and hover
#     driver.execute_script("arguments[0].scrollIntoView(true);", more_element)
#     actions = ActionChains(driver)
#     actions.move_to_element(more_element).perform()
#
#     # Wait for 'Electric Vehicles' and click
#     electric_vehicles = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[text()='Electric Vehicles']"))
#     )
#     electric_vehicles.click()
#
#     # ✅ Add an assertion to confirm navigation success
#     assert "Electric Vehicles Store" in driver.title, "Navigation to Electric Vehicles failed!"
#
#     print("Test completed successfully!")

def test_mouse_hover(setup_browser):
    driver = setup_browser

    # Close the login popup if present
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='✕']"))
        )
        close_button.click()
    except Exception as e:
        print("Login popup did not appear or could not be closed.")

    # Hover over 'Two Wheelers'
    more_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Two Wheelers']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", more_element)
    actions = ActionChains(driver)
    actions.move_to_element(more_element).perform()

    # Wait for 'Electric Vehicles' and click
    electric_vehicles = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Electric Vehicles']"))
    )
    electric_vehicles.click()
    time.sleep(5)

    # ✅ Updated assertion for correct verification
    assert "electric-scooters-store" in driver.current_url, "Navigation to Electric Vehicles failed!"
    assert "Electric Scooter Buy Online From Flipkart | Electric Vehicle Online 16-Feb-25" in driver.title, "Page title does not match!"

    print("Test completed successfully!")






