from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("file:///home/athul/Documents/selenium-demo/fruit-salad.html")

ticks = Select(driver.find_element_by_id('fruits'))
#Selecting Options in different ways
ticks.select_by_index(0)
ticks.select_by_value ('cranberry')
ticks.select_by_visible_text('Elderberry')
ticks.select_by_index(6)

