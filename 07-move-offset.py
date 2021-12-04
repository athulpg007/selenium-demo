from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.apress.com")

#Offset positions of x and y
x =268
y =66
#Move element with offset position defined
webdriver.ActionChains(driver).move_by_offset(x,y).perform()