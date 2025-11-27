from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    driver.find_element("id", "not exist button")
except NoSuchElementException as nse:
    print("Element not found!", nse.msg)
