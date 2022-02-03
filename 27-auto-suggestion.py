from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time
driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("https://www.google.com")

search = driver.find_element(By.NAME, 'q').send_keys("Bangalore")
time.sleep(5)

results = driver.find_elements(By.XPATH, "//u1[@class='G43f7e']/li")

print(len(results))