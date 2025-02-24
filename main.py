# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=options)
# driver.get("")
# driver.find_element(By.ID,"sidebar content").click()
# import time
# from  selenium import webdriver
# from selenium .webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://automationstepbystep.com/")
# WebDriverWait(driver,20).until(
# driver.find_element(By.LINK_TEXT,"Show Me")).click()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC  # Import this
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.select import Select

# Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")
search_field = driver.find_element("xpath","//input[type = text]")
search_field.send_keys("oneplus headphone")
# driv"Islamabad"er.find_element(By.CSS_SELECTOR,"[type='search']").click()

# search_element = driver.find_element(By.XPATH,"//input[@class ='form-control py-2']")
# search_element.send_keys("Islamabad")
# search_element.clear()
# search_element.send_keys("Rawalpindi")

# check_boxes=driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")
# print(check_boxes)
# print(len(check_boxes))
# for check_box in check_boxes:
#     if(check_boxes.index(check_box)+1 !=2):
#       check_box.click()
# static_dropdowm = driver.find_element(By.ID, "dropdown-class-example")
# select= Select(static_dropdowm)
# select.select_by_index(2)
# time.sleep(2)
# select.select_by_visible_text("Option1")
# time.sleep(2)
# select.select_by_value("option3")
# wait = webdriver
# blinking_link = driver.find_element(By.CLASS_NAME , 'blinkingText')


# print(blinking_link.get_attribute("href"))
deal_banners = driver.find_elements(By.XPATH,"//div[@data-clone='false']//a")
print(f"total number of deals :{len(deal_banners)}")
for deal_banner in deal_banners:
    print(deal_banner.get_attribute("href"))






# Use WebDriverWait with expected_conditions
# WebDriverWait(driver,
    WebDriverWait(driver,5,0.2).until()
    EC.visibility_of_element_located((By.LINK_TEXT, "Show Me")).click()














