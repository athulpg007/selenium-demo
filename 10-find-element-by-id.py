from selenium import webdriver
driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("file:///home/athul/Documents/selenium-demo/employee.html")

Employee_form = driver.find_element_by_id ('EmployeeForm')
