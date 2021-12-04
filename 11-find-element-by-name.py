from selenium import webdriver
driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("file:///home/athul/Documents/selenium-demo/employee2.html")

#Locating first element
employee = driver.find_element_by_name('employee_name')
#Locating second element
email = driver.find_element_by_name('email')