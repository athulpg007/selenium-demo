#Importing selenium libraries in python
from selenium import webdriver

#Opening web Firefox browser using webdriver
driver=webdriver.Firefox()

#Adding URL to open in browser
driver.get("http://www.google.com")
print(driver.title)


# Close Firefox browser
#driver.quit()