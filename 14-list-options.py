from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("file:///home/athul/Documents/selenium-demo/blood-group.html")

# First Select ID of drop-down
select_list=Select(driver.find_element_by_id('bld_grp'))
# select by visible text
select_list.select_by_visible_text('O type')
