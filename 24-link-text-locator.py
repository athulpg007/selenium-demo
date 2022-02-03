from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("https://athulpg007.github.io")

search = driver.find_element(By.LINK_TEXT, 'Personal').click()
