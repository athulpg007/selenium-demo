from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("https://athulpg007.github.io")

try:
	search = driver.find_element(By.PARTIAL_LINK_TEXT, 'Photos').click()
except NoSuchElementException:
	print("No such elemenet")

