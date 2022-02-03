from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("https://www.google.com")

search = driver.find_element(By.LINK_TEXT, 'How Search works').click()
