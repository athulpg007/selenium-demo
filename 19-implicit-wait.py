# Import Selenium Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Time frame set for 10 seconds
timeout =10
# Creating Firefox driver instance
driver = webdriver.Firefox()
# Calling Implicit wait function
driver.implicitly_wait(timeout) #driver.implicitly_wait(10) Time frame can
# diretly be set
# Go to URL www.apress.com

driver.get("http://google.com")
print("It's an Implicit Wait")

# Retrieving ID element
new_element = driver.find_element_by_name("q")
# Type "Python with selenium" in search bar
new_element.send_keys("Athul Pradeepkumar Girija")
# Submit text in search bar
new_element.submit()
# Close Firefox browser
