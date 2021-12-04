from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("https://apress.com")

try:
        web1 =driver.find_element_by_id("privacy")
        web1.click()

except NoSuchElementException as exception:
        print ("Web Element is not Available in the given Web Page.")