from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.apress.com")

# Go to button
web_element=driver.find_element_by_link_text("Account")

#Clicking on the button to be selected
web_element.click()