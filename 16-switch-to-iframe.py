from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("file:///home/athul/Documents/selenium-demo/iframe.html")

# Switch to the frame with id attribute
driver.switchTo().frame("new_frame")
